from sqlalchemy import Column, Integer, ForeignKey, String
from db.db import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    username = Column(String(50), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=False)
