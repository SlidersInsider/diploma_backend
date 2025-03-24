import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from db.models.file import File

UPLOAD_DIR = "uploads"

# Функция для сохранения файла на сервер
def save_file(file: UploadFile, project_id: int, user_id: int, db: Session):
    os.makedirs(UPLOAD_DIR, exist_ok=True)  # Создать папку, если её нет
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Записываем файл в указанную директорию
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Сохраняем запись в БД
    new_file = File(
        project_id=project_id,
        user_id=user_id,
        filename=file.filename,
        file_path=file_path,
        encryption_key="s3cr3tK3y"  # Тут должна быть логика шифрования
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    db.close()

    return new_file

def remove_file(file, db: Session):
    # Удаляем физический файл с диска
    if os.path.exists(file.file_path):
        os.remove(file.file_path)

    # Удаляем запись из базы данных
    db.delete(file)
    db.commit()