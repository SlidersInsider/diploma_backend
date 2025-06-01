import os

from Crypto.Signature.pss import MGF1
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from db.models import User, UserProject
from db.models.file import File
from db.models.key import Key


UPLOAD_DIR = "uploads"

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

def save_file(file: UploadFile, project_id: int, user_id: int, encrypted_key_b64: str, db: Session):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # ✅ Сохраняем файл как есть (он уже зашифрован на клиенте)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # ✅ Сохраняем файл в БД
    new_file = File(
        project_id=project_id,
        user_id=user_id,
        filename=file.filename,
        file_path=file_path,
        encryption_key=encrypted_key_b64
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    # ✅ Сохраняем ключ для владельца
    db.add(Key(
        user_id=user_id,
        file_id=new_file.id,
        project_id=project_id,
        encrypted_key=encrypted_key_b64
    ))

    db.commit()
    return new_file


def remove_file(file, db: Session):
    # Удаляем физический файл с диска
    if os.path.exists(file.file_path):
        os.remove(file.file_path)

    # Удаляем запись из базы данных
    db.delete(file)
    db.commit()

def download_file(file, user_id: int, db: Session) -> dict:
    key_entry = db.query(Key).filter(
        Key.file_id == file.id,
        Key.user_id == user_id
    ).first()

    if not key_entry:
        raise HTTPException(status_code=403, detail="У вас нет доступа к этому файлу")

    if not os.path.exists(file.file_path):
        raise HTTPException(status_code=404, detail="Файл не найден на диске")

    with open(file.file_path, "rb") as f:
        encrypted_file_data = f.read()

    return {
        "filename": file.filename,
        "encrypted_key": key_entry.encrypted_key,  # уже в base64
        "file_data": base64.b64encode(encrypted_file_data).decode("utf-8")
    }


def share_project_keys_with_user(project_id: int, new_user_id: int, user_public_key_str: str, manager_private_key_str: str, db):
    decoded_private_pem = base64.b64decode(manager_private_key_str).decode("utf-8")
    private_key = RSA.import_key(decoded_private_pem)
    rsa_decryptor = PKCS1_OAEP.new(private_key)

    decoded_public_pem = base64.b64decode(user_public_key_str).decode("utf-8")
    public_key = RSA.import_key(decoded_public_pem)
    rsa_encryptor = PKCS1_OAEP.new(public_key)

    files = db.query(File).filter(File.project_id == project_id).all()

    for file in files:
        # Дешифруем симметричный ключ
        encrypted_sym_key_bytes = base64.b64decode(file.encryption_key)
        sym_key = rsa_decryptor.decrypt(encrypted_sym_key_bytes)

        # Шифруем симметричный ключ для нового пользователя
        re_encrypted_key = rsa_encryptor.encrypt(sym_key)
        re_encrypted_key_b64 = base64.b64encode(re_encrypted_key).decode("utf-8")

        # Добавляем запись в таблицу keys
        key_entry = Key(
            user_id=new_user_id,
            file_id=file.id,
            project_id=project_id,
            encrypted_key=re_encrypted_key_b64
        )
        db.add(key_entry)

    db.commit()
