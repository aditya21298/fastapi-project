from datetime import datetime
import email
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

from app.models import Post, User

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id: int
    email : EmailStr
    created_at : datetime

    class Config:
        orm_mode = True




class postResponse(PostBase):
    id : int
    created_at : datetime
    user_id : int
    user : UserOut
    
#Response from above class is sqlalchemy(not in dict) so below config is used to convert it into pydantic model.
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: postResponse
    votes: int

    class Config:
        orm_mode = True




class UserLogin(BaseModel):

    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
 post_id : int
 dir : conint(le=1)
    