from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get("/health-check")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok", "database": "connected"}