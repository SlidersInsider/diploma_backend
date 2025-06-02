from fastapi import APIRouter, UploadFile, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models import User, UserProject
from services.file_service import save_file, remove_file, download_file
from db.models.file import File
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_files(
        db: Session = Depends(get_db)
):
    files = db.query(File).all()
    return files

@router.get("/project/{project_id}")
def get_files_by_project(
        project_id: int,
        db: Session = Depends(get_db)
):
    files = db.query(File).filter(File.project_id == project_id).all()
    if not files:
        raise HTTPException(status_code=404, detail="Файлы для проекта не найдены")
    return files

@router.get("/user/{user_id}")
def get_files_by_user(
        user_id: int,
        db: Session = Depends(get_db)
):
    files = db.query(File).filter(File.user_id == user_id).all()
    if not files:
        raise HTTPException(status_code=404, detail="Файлы пользователя не найдены")
    return files

@router.post("/")
def upload_file(
    file: UploadFile,
    project_id: int = Form(...),
    user_id: int = Form(...),
    public_key: str = Form(...),
    db: Session = Depends(get_db)
):
    saved_file = save_file(file, project_id, user_id, public_key, db)

    project_users = db.query(User).join(UserProject).filter(UserProject.project_id == project_id).all()

    return {
        "message": "Файл загружен!",
        "file_id": saved_file.id,
        "project_users": [
            {"id": user.id, "username": user.username, "public_key": user.public_key}
            for user in project_users
        ]
    }

@router.delete("/{file_id}")
def delete_file(
        file_id: int,
        db: Session = Depends(get_db)
):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="Файл не найден")
    removed_file = remove_file(file, db)

    return {"message": "Файл успешно удалён", "file": removed_file}

@router.get("/{file_id}")
def get_file_by_id(
        file_id: int,
        db: Session = Depends(get_db)
):
    file = db.query(File).filter(File.id == file_id).first()

    if not file:
        raise HTTPException(status_code=404, detail="Файл не найден")

    return file

@router.post("/download/{file_id}")
def download(
    file_id: int,
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    file = db.query(File).filter(File.id == file_id).first()
    if not file:
        raise HTTPException(status_code=404, detail="Файл не найден")

    return download_file(file, user_id, db)

@router.put("/update-file/{file_id}")
def update_file(
    file_id: int,
    file: UploadFile,
    db: Session = Depends(get_db)
):
    existing_file = db.query(File).filter(File.id == file_id).first()
    if not existing_file:
        raise HTTPException(status_code=404, detail="Файл не найден")

    file_path = existing_file.file_path

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден на сервере")

    with open(file_path, "wb") as f:
        content = file.file.read()
        f.write(content)

    return {"message": "Файл успешно обновлен", "file_id": existing_file.id}

