# db/models/key.py
from sqlalchemy import Column, Integer, String, ForeignKey
from db.db import Base

class Key(Base):
    __tablename__ = "keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    file_id = Column(Integer, ForeignKey("files.id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    encrypted_key = Column(String(4096), nullable=False)  # base64
