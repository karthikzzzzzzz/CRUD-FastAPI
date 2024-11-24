from fastapi import Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from schemas import UserResponse, Request
import models
from hashing import Hash



def create_user_details(request: Request, db: Session = Depends(get_db)):
    hashed_password = Hash.hash_password(request.password)
    new_user = models.Login(
        username=request.username,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def retireve_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Login).filter(models.Login.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} not found"
        )
    return user
