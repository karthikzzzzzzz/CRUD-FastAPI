# schemas.py

from pydantic import BaseModel
from typing import Optional

class Aceess(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class Request(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Blogreq(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

class UserResponse(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    owner: UserResponse  # Include owner details

    class Config:
        orm_mode = True

class Output(BaseModel):
    username: str
    email: str

class Response(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True
