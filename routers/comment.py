from datetime import datetime
from typing import List

from fastapi import Depends, status, Response, HTTPException, APIRouter
import schemas, models, database
from database import database

router = APIRouter(tags=["Comment"])


@router.post("/post/{post_id}/comment", status_code=status.HTTP_201_CREATED)
async def add_comment(post_id: int, comment: schemas.Comment):
    query = models.Post.select().where(post_id == models.Post.c.id)
    find_post = await database.fetch_one(query=query)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found")

    query = models.Comment.insert().values(post_id=post_id, username=comment.username, \
                                           content=comment.content, time_=datetime.now())
    last_record_id = await database.execute(query)
    return f"Comment {last_record_id} added"


@router.get("/post/{post_id}/comment", status_code=status.HTTP_200_OK)
async def browse_comment(post_id: int):
    query = models.Post.select().where(post_id == models.Post.c.id)
    find_post = await database.fetch_one(query=query)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found")
    query = models.Comment.select().where(post_id == models.Comment.c.post_id)
    return await database.fetch_all(query=query)
