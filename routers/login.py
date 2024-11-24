# login.py

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import  Token
from models import Login
from hashing import Hash
from routers.token import create_access_token
from database import get_db

app = APIRouter()

@app.post("/login", response_model=Token)
def login_user(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(Login).filter(Login.email == request.username).first()
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
