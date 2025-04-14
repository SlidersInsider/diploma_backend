from pydantic import BaseModel

class RequestModel(BaseModel):
    user_id: int
    username: str
    project_id: int
    manager_id: int
