from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.user import User
from db.models.role import Role
from passlib.context import CryptContext
from schemas.user import UserModel
from schemas.role import RoleModel

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user(
        user: UserModel,
        db: Session = Depends(get_db)
):
    hashed_password = pwd_context.hash(user.password)

    role = db.query(Role).filter(Role.name == user.role).first()
    if not role:
        raise HTTPException(status_code=400, detail="Роль не найдена")

    new_user = User(username=user.username, password_hash=hashed_password, role_id=role.id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Пользователь создан", "user": new_user}


@router.delete("/{user_id}")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    db.delete(user)
    db.commit()

    return {"message": "Пользователь удалён"}


@router.put("/{user_id}/role")
def update_user_role(
        user_id: int,
        role: RoleModel,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    role = db.query(Role).filter(Role.name == role.name).first()
    if not role:
        raise HTTPException(status_code=400, detail="Роль не найдена")

    user.role_id = role.id
    db.commit()

    return {"message": "Роль пользователя обновлена", "user": user}


@router.get("/")
def get_users(
        db: Session = Depends(get_db)
):
    return db.query(User).all()


@router.get("/{username}")
def get_user_by_name(
        username: str,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return user

@router.get("/{user_id}")
def get_user_by_id(
        user_id: int,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return user
