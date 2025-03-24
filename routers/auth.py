from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.user import User
from db.models.role import Role
from schemas.user import UserCreate, UserLogin, Token
from services.security import hash_password, verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(
        user_data: UserCreate,
        db: Session = Depends(get_db)
):
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    # Если роль не указана, устанавливаем роль "worker"
    role_id = user_data.role_id if user_data.role_id else db.query(Role).filter(Role.name == "worker").first().id

    if not role_id:
        raise HTTPException(status_code=400, detail="Указанная роль не существует")

    new_user = User(
        username=user_data.username,
        password_hash=hash_password(user_data.password),
        role_id=role_id
    )
    db.add(new_user)
    db.commit()

    return {"message": "Регистрация прошла успешно"}

@router.post("/login", response_model=Token)
def login(
        user_data: UserLogin,
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == user_data.username).first()

    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
