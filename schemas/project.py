from pydantic import BaseModel

class ProjectModel(BaseModel):
    name: str
    description: str
    creator_id: int