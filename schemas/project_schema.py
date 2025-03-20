from pydantic import BaseModel
from typing import Optional

# Входная схема (создание проекта)
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None  # Используем Optional вместо "|"

# Выходная схема (ответ API)
class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
