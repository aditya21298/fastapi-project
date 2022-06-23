
from operator import index
from re import T
from fastapi import FastAPI
from random import randrange
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user,auth,vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware


#Binding the models
#no longer needed due to adding alembic models
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#origins means websites that can reach our api
origins = ["*"]

#CORS policy code snippet
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


my_posts= [{"title":"title of post 1", "content": "content of post 1", "id":1},{"title":"Cricket Shots", "content": "Upper cut", "id":2}]

def find_post(id):
   for p in my_posts:
       if p["id"] ==id:
           return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i

#routing
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}


