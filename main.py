from routers import user, blog,login
from fastapi import  FastAPI
import models
from database import engine

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.app, tags=['Login'])
app.include_router(blog.app, tags=['Blogs'])
app.include_router(user.app, tags=['Users'])
