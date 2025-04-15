from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.user_project import UserProject
from db.models.user import User
from db.models.project import Project
from db.models.request import Request
from schemas.user_project import UserProjectModel
from services.file_service import share_project_keys_with_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_user_to_project(
        user_id: int = Form(...),
        project_id: int = Form(...),
        user_public_key: str = Form(...),       # публичный ключ нового пользователя
        manager_private_key: str = Form(...),   # приватный ключ руководителя
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    project = db.query(Project).filter(Project.id == project_id).first()

    if not user or not project:
        raise HTTPException(status_code=404, detail="Пользователь или проект не найдены")

    user_project = UserProject(user_id=user_id, project_id=project_id)
    db.add(user_project)

    request = db.query(Request).filter(
        Request.user_id == user_id,
        Request.project_id == project_id
    ).first()

    if request:
        db.delete(request)

    # Перешифровка ключей файлов проекта для нового пользователя
    try:
        share_project_keys_with_user(
            project_id=project_id,
            new_user_id=user_id,
            user_public_key_str=user_public_key,
            manager_private_key_str=manager_private_key,
            db=db
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка шифрования ключей: {str(e)}")

    db.commit()
    return {"message": "Пользователь успешно добавлен на проект и ключи зашифрованы"}


@router.delete("/")
def remove_user_from_project(
        up: UserProjectModel,
        db: Session = Depends(get_db)
):
    user_project = db.query(UserProject).filter(
        UserProject.user_id == up.user_id,
        UserProject.project_id == up.project_id
    ).first()

    if not user_project:
        raise HTTPException(status_code=404, detail="Запись не найдена")

    db.delete(user_project)
    db.commit()

    return {"message": "Пользователь успешно удален с проекта"}

@router.get("/project/{project_id}")
def get_users_by_project(
        project_id: int,
        db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Проект не найден")

    users = db.query(User).join(UserProject, User.id == UserProject.user_id).filter(
        UserProject.project_id == project_id).all()

    return {"project": project.name, "users": users}
