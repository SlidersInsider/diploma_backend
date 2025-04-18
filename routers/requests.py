from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db.models.request import Request

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{manager_id}")
def get_requests_by_manager(manager_id: int, db: Session = Depends(get_db)):
    requests = db.query(Request).filter(Request.manager_id == manager_id).all()
    return requests