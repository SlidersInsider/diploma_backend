import base64

from Crypto.PublicKey import RSA
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

    # Получаем роль
    role_id = user_data.role_id if user_data.role_id else db.query(Role).filter(Role.name == "worker").first().id

    if not role_id:
        raise HTTPException(status_code=400, detail="Указанная роль не существует")

    # Генерируем RSA-ключи (2048 бит)
    key = RSA.generate(2048)

    # Публичный ключ сохраняем в base64
    public_key_b64 = base64.b64encode(key.publickey().export_key()).decode("utf-8")

    # Приватный ключ кодируем в base64, но возвращаем обычной строкой (для отображения)
    private_key_b64 = base64.b64encode(key.export_key()).decode("utf-8")
    # private_key_pem = key.export_key().decode("utf-8")
    # public_key_pem = key.publickey().export_key().decode("utf-8")

    new_user = User(
        username=user_data.username,
        password_hash=hash_password(user_data.password),
        role_id=role_id,
        public_key=public_key_b64  # сохраняем публичный ключ
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "Регистрация прошла успешно",
        "public_key": public_key_b64,  # Возвращаем публичный ключ пользователю
        "private_key": private_key_b64  # Возвращаем приватный ключ пользователю
    }


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
