from sqlalchemy import Column, Integer, ForeignKey
from db.db import Base

class UserProject(Base):
    __tablename__ = "user_projects"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
