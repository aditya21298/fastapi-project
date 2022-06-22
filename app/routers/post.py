from typing import List, Optional

from app import oauth2
from ..import models,schemas,utils, oauth2
from fastapi import Body, FastAPI, Response, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from sqlalchemy import func


#Using routers to change "app" decorator to router
router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user :int = Depends(oauth2.get_current_user),
limit : int = 10, skip : int = 0, search : Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts """)
    # posts= cursor.fetchall()
    # print(posts)
 #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return results

@router.post("/", response_model=schemas.postResponse)
def create_posts(post : schemas.PostCreate, db: Session = Depends(get_db),
 current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title,
    # post.content, post.published))
    # new_post= cursor.fetchone()
    # conn.commit()
    new_post= models.Post(user_id= current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}",response_model=schemas.PostOut)
def get_posts(id: int, db: Session = Depends(get_db), 
     current_user :int = Depends(oauth2.get_current_user)):
    posts=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(
            models.Post.id).filter(models.Post.id == id).first()
    # cursor.execute("""SELECT * FROM posts WHERE id= %s""",(str(id)))
    # post_test=cursor.fetchone()
    # post = find_post(id)
    # print(post_test)
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with {id} not found")
    return posts

@router.delete("/{id}")
def delete_posts(id:int, db: Session = Depends(get_db),
      current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s returning *""",(str(id)))
    # del_post=cursor.fetchone
    # conn.commit()
    # index= find_index_post(id)
    posts_query = db.query(models.Post).filter(models.Post.id == id)
    posts = posts_query.first()
    if posts == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} does not exist")
    
    if posts.user_id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized to perform requested action")
    #append delete to the original query
    posts_query.delete(synchronize_session=False)
    db.commit()
    # my_posts.pop(index)
    return Response (status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.postResponse)
def update_post(id:int, user_post:schemas.PostBase, db: Session = Depends(get_db),
     current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title= %s, content=%s, published=%s WHERE id=%s returning*""", (post.title,
    # post.content, post.published, str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    # index= find_index_post(id)
    posts_query = db.query(models.Post).filter(models.Post.id == id)
    posts= posts_query.first()
    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} does not exist")
    
    if posts.user_id != current_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized to perform requested action")
    posts_query.update(user_post.dict(), synchronize_session=False)
    db.commit()

    #  post_dict=post.dict()
    #  post_dict['id']=id
    #  my_posts[index]= post_dict
    return posts_query.first()