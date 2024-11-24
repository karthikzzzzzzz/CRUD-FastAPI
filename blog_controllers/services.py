from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import Blogreq


def create_blog_post(request: Blogreq, db: Session = Depends(get_db)):
    user = db.query(models.Login).filter(models.Login.id == request.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {request.user_id} not found"
        )
    new_blog = models.Blog(
        title=request.title,
        content=request.content,
        user_id=request.user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def retrieve_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def retreive_id_blogs(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {id} not found"
        )
    return blog

def delete_blogs(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {id} not found"
        )
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with ID {id} deleted successfully"}

def update_blogs(request: Blogreq, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == request.id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID {request.id} not found"
        )
    blog.title = request.title
    blog.content = request.content
    db.commit()
    db.refresh(blog)
    return blog

