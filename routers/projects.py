from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.project import Project

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_project(
        name: str,
        description: str,
        db: Session = Depends(get_db)
):
    existing_project = db.query(Project).filter(Project.name == name).first()
    if existing_project:
        raise HTTPException(status_code=400, detail="Проект с таким именем уже существует")

    new_project = Project(name=name, description=description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

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

