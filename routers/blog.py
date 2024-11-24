from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from blog_controllers.services import create_blog_post, delete_blogs, retreive_id_blogs, retrieve_blogs, update_blogs
from routers.oauth import get_current_user
from schemas import Blogreq, BlogResponse, Request

from database import get_db

app = APIRouter()


@app.post('/blog', response_model=BlogResponse)
def create_blog(request: Blogreq, db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    return create_blog_post(request,db)


@app.get('/all',response_model=list[BlogResponse])
def get_all(db: Session = Depends(get_db),current_user: str= Depends(get_current_user)):
    return retrieve_blogs(db)


@app.get('/all/{id}',  response_model=BlogResponse)
def get_by_id(id: int, db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    return retreive_id_blogs(id, db)


@app.delete('/delete/{id}')
def delete_blog(id: int, db: Session = Depends(get_db),current_user: str= Depends(get_current_user)):
    return delete_blogs(id, db)


@app.put('/update_blog', response_model=BlogResponse)
def update_blog(request: Blogreq, db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    return update_blogs(request, db)