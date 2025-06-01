from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
