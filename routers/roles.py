from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.role import Role, UserRole
from schemas.role import RoleModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_role(
        role: RoleModel,
        db: Session = Depends(get_db)
):
    if role.name not in UserRole.__members__:
        raise HTTPException(status_code=400, detail="Неверное название роли")

    existing_role = db.query(Role).filter(Role.name == role.name).first()
    if existing_role:
        raise HTTPException(status_code=400, detail="Роль уже существует")

    new_role = Role(name=UserRole[role.name])
    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return {"message": "Роль успешно добавлена", "role": new_role}

@router.delete("/{role_id}")
def delete_role(
        id: int,
        db: Session = Depends(get_db)
):
    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Роль не найдена")

    db.delete(role)
    db.commit()

    return {"message": "Роль успешно удалена"}

@router.get("/")
def get_all_roles(
        db: Session = Depends(get_db)
):
    roles = db.query(Role).all()
    return {"roles": roles}

@router.get("/{role_id}")
def get_role_by_id(
        role_id: int,
        db: Session = Depends(get_db)
):
    role = db.query(Role).filter(Role.id == role_id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Роль не найдена")

    return role
