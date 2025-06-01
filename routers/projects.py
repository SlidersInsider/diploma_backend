from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models import User, Role, UserProject
from db.models.project import Project
from schemas.project import ProjectModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_project(
        project: ProjectModel,
        db: Session = Depends(get_db)
):
    # Проверка на существование проекта с таким именем
    existing_project = db.query(Project).filter(Project.name == project.name).first()
    if existing_project:
        raise HTTPException(status_code=400, detail="Проект с таким именем уже существует")

    # Получаем пользователя
    user = db.query(User).filter(User.id == project.creator_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Проверяем его роль
    role = db.query(Role).filter(Role.id == user.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Роль пользователя не найдена")

    if role.name == "worker":
        raise HTTPException(status_code=403, detail="Рабочий не может создавать проект")

    # Создание проекта
    new_project = Project(
        name=project.name,
        description=project.description,
        creator_id=project.creator_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # Добавляем создателя как участника проекта
    user_project = UserProject(user_id=project.creator_id, project_id=new_project.id)
    db.add(user_project)
    db.commit()

    return {"message": "Проект создан", "project": new_project}

@router.delete("/{project_id}")
def delete_project(
        project_id: int,
        db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Проект не найден")

    db.delete(project)
    db.commit()

    return {"message": "Проект удалён"}

@router.get("/")
def get_all_projects(
        db: Session = Depends(get_db)
):
    projects = db.query(Project).all()
    return projects

@router.get("/{project_name}")
def get_project_by_name(
        project_name: str,
        db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.name == project_name).first()
    if not project:
        raise HTTPException(status_code=404, detail="Проект не найден")

    return project

@router.get("/{project_id}")
def get_project_by_id(
        project_id: int,
        db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Проект не найден")

    return project

@router.get("/user/{user_id}")
def get_user_projects(user_id: int, db: Session = Depends(get_db)):
    user_projects = db.query(Project).join(UserProject).filter(UserProject.user_id == user_id).all()

    if not user_projects:
        raise HTTPException(status_code=404, detail="Проекты для пользователя не найдены")

    return user_projects