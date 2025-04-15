import os
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from db.models import User, UserProject
from db.models.file import File
from db.models.key import Key
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64


UPLOAD_DIR = "uploads"

def save_file(file: UploadFile, project_id: int, user_id: int, public_key_str: str, db: Session):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Генерация симметричного ключа
    symmetric_key = get_random_bytes(32)

    # Шифруем файл для владельца
    decoded_pem = base64.b64decode(public_key_str).decode("utf-8")
    public_key = RSA.import_key(decoded_pem)
    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_key = rsa_cipher.encrypt(symmetric_key)
    encrypted_key_b64 = base64.b64encode(encrypted_key).decode("utf-8")

    # Шифруем содержимое файла AES
    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX)
    ciphertext, tag = aes_cipher.encrypt_and_digest(file.file.read())

    with open(file_path, "wb") as f:
        f.write(aes_cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

    # Сохраняем файл
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

    # Сохраняем ключ для владельца
    db.add(Key(
        user_id=user_id,
        file_id=new_file.id,
        project_id=project_id,
        encrypted_key=encrypted_key_b64
    ))

    # Получаем всех участников проекта
    project_users = db.query(User).join(UserProject).filter(UserProject.project_id == project_id).all()

    for participant in project_users:
        if participant.id == user_id or not participant.public_key:
            continue  # Пропускаем владельца и тех, у кого нет публичного ключа


        try:
            decoded_part_pem = base64.b64decode(public_key_str).decode("utf-8")
            user_pubkey = RSA.import_key(decoded_part_pem)
            rsa_cipher = PKCS1_OAEP.new(user_pubkey)
            encrypted_key = rsa_cipher.encrypt(symmetric_key)
            encrypted_key_b64 = base64.b64encode(encrypted_key).decode("utf-8")

            db.add(Key(
                user_id=participant.id,
                file_id=new_file.id,
                project_id=project_id,
                encrypted_key=encrypted_key_b64
            ))
        except Exception as e:
            print(f"Ошибка при шифровании ключа для пользователя {participant.id}: {e}")

    db.commit()
    return new_file



def remove_file(file, db: Session):
    # Удаляем физический файл с диска
    if os.path.exists(file.file_path):
        os.remove(file.file_path)

    # Удаляем запись из базы данных
    db.delete(file)
    db.commit()

def download_file(file, user_id: int, private_key_str: str, db: Session):
    # Получаем нужный зашифрованный ключ из таблицы keys
    key_entry = db.query(Key).filter(
        Key.file_id == file.id,
        Key.user_id == user_id
    ).first()

    if not key_entry:
        raise HTTPException(status_code=403, detail="У вас нет доступа к этому файлу")

    # Расшифровываем симметричный ключ приватным RSA-ключом
    decoded_pem = base64.b64decode(private_key_str).decode("utf-8")
    private_key = RSA.import_key(decoded_pem)
    rsa_cipher = PKCS1_OAEP.new(private_key)

    encrypted_key_bytes = base64.b64decode(key_entry.encrypted_key)
    try:
        symmetric_key = rsa_cipher.decrypt(encrypted_key_bytes)
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверный приватный ключ")

    # Открываем файл и расшифровываем
    with open(file.file_path, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = aes_cipher.decrypt_and_verify(ciphertext, tag)

    # Сохраняем расшифрованный файл
    decrypted_file_path = f"downloads/decrypted_{file.filename}"
    os.makedirs("downloads", exist_ok=True)

    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path


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
