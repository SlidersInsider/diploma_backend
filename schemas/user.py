from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role_id: int
    public_key: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserModel(BaseModel):
    username: str
    password: str
    role: str
