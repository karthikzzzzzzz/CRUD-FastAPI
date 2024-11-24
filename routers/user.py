from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session

from schemas import UserResponse, Request

from database import get_db

from users.controllers import create_user_details, retireve_user_by_id

app=APIRouter()




@app.post('/user', response_model=UserResponse)
def create_user(request: Request, db: Session = Depends(get_db)):
    return create_user_details(request,db)
    


@app.get('/user/{id}',  response_model=UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return retireve_user_by_id(id,db)
