from datetime import datetime
from typing import List

from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

import schemas
import models
import database

router = APIRouter(tags=["Comment"])

@router.post("/post/{post_id}/comment", status_code=status.HTTP_201_CREATED)
def add_comment(post_id, request: schemas.Comment, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    new_comment = models.Comment(username=request.username, content=request.content, post_id=post_id, time_=datetime.now())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/post/{post_id}/comment", status_code=status.HTTP_200_OK)
def browse_comment(post_id, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    comments = db.query(models.Comment).filter(models.Comment.post_id == post_id).all()
    return comments