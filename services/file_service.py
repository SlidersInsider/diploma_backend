import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from db.models.file import File
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

UPLOAD_DIR = "uploads"

def save_file(file: UploadFile, project_id: int, user_id: int, public_key_str: str, db: Session):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Генерация симметричного ключа (AES)
    symmetric_key = get_random_bytes(32)  # 256-битный ключ AES

    # Шифрование симметричного ключа публичным ключом (RSA)
    public_key = RSA.import_key(public_key_str)
    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_symmetric_key = rsa_cipher.encrypt(symmetric_key)
    encrypted_key_b64 = base64.b64encode(encrypted_symmetric_key).decode("utf-8")

    # Шифрование файла симметричным ключом AES
    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX)
    ciphertext, tag = aes_cipher.encrypt_and_digest(file.file.read())

    # Запись зашифрованного файла на диск
    with open(file_path, "wb") as f:
        f.write(aes_cipher.nonce)  # Сохраняем nonce (инициализационный вектор)
        f.write(tag)               # Сохраняем тег проверки целостности
        f.write(ciphertext)        # Сохраняем зашифрованный контент

    # Сохраняем запись в БД
    new_file = File(
        project_id=project_id,
        user_id=user_id,
        filename=file.filename,
        file_path=file_path,
        encryption_key=encrypted_key_b64  # Сохраняем зашифрованный симметричный ключ в base64
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file


def remove_file(file, db: Session):
    # Удаляем физический файл с диска
    if os.path.exists(file.file_path):
        os.remove(file.file_path)

    # Удаляем запись из базы данных
    db.delete(file)
    db.commit()

def download_file(file, private_key_str: str):
    # Дешифруем симметричный ключ приватным ключом RSA
    private_key = RSA.import_key(private_key_str)
    rsa_cipher = PKCS1_OAEP.new(private_key)

    encrypted_key_bytes = base64.b64decode(file.encryption_key)
    symmetric_key = rsa_cipher.decrypt(encrypted_key_bytes)

    # Открываем зашифрованный файл для чтения
    with open(file.file_path, "rb") as f:
        nonce = f.read(16)  # nonce (инициализационный вектор) - 16 байт
        tag = f.read(16)    # тег проверки целостности - 16 байт
        ciphertext = f.read()  # оставшееся - зашифрованное содержимое

    # Дешифруем содержимое файла
    aes_cipher = AES.new(symmetric_key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = aes_cipher.decrypt_and_verify(ciphertext, tag)

    # Записываем расшифрованный файл временно и возвращаем его пользователю
    decrypted_file_path = f"downloads/decrypted_{file.filename}"
    os.makedirs("downloads", exist_ok=True)

    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path