
from database import Base
from sqlalchemy import Column,Integer,String,   ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))

    owner=relationship('Login',back_populates='blogs')

class Login(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    password=Column(String)
    email=Column(String)

    blogs=relationship('Blog',back_populates='owner')
    
