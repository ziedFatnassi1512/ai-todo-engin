from fastapi import  Depends ,APIRouter,status
from sqlalchemy.orm import Session
from sqlalchemy import text
import models
import schema
from database import get_db


router =APIRouter()

@router.post("/" ,status_code=status.HTTP_201_CREATED )
def create_user(user: schema.User , db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user