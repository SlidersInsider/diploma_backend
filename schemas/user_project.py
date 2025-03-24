from pydantic import BaseModel

class UserProjectModel(BaseModel):
    user_id: int
    project_id: int