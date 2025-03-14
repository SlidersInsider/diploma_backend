from sqlalchemy import Column, Integer, Enum
from db.db import Base
import enum


class UserRole(enum.Enum):
    admin = "admin"
    manager = "manager"
    worker = "worker"


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(UserRole), unique=True, nullable=False)
