from typing import List
from fastapi import Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
import schemas
import models
import database

router = APIRouter(tags=["Post"])

# Browse all posts
@router.get("/post", response_model=List[schemas.ShowPosts], status_code=status.HTTP_200_OK)
def browse_post(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()
    return posts

# Read a post by post_id
@router.get("/post/{post_id}", response_model=schemas.ShowPost, status_code=status.HTTP_200_OK)
def read_post(post_id, response: Response, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} does not exist.")
    return post

# Add a new post
@router.post("/post", status_code=status.HTTP_201_CREATED)
def add_post(request: schemas.Post, db: Session = Depends(database.get_db)):
    new_post = models.Post(author=request.author, title=request.title, content=request.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Edit a post by post_id
@router.patch("/post/{post_id}", status_code=status.HTTP_202_ACCEPTED)
def edit_post(post_id, request: schemas.Post, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    post.update({"author": request.author})
    post.update({"title": request.title})
    post.update({"content": request.content})
    db.commit()
    return "updated"

# Delete a post by post_id
@router.delete("/post/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return "done"
