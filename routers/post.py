from datetime import datetime
from typing import List

from fastapi import Depends, status, Response, HTTPException, APIRouter
import schemas, models, database
from database import database

router = APIRouter(tags=["Post"])


@router.get("/post", status_code=status.HTTP_200_OK)
async def browse_post():
    query = models.Post.select()
    return await database.fetch_all(query=query)


@router.get("/post/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int):
    query = models.Post.select().where(post_id == models.Post.c.id)
    post = await database.fetch_one(query=query)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found")
    return {**post}


@router.post("/post", status_code=status.HTTP_201_CREATED)
async def add_post(post: schemas.Post):
    query = models.Post.insert().values(title=post.title, author=post.author, \
                                        content=post.content, time_=datetime.now())
    last_record_id = await database.execute(query)
    return {**post.dict(), "id": last_record_id}


@router.patch("/post/{post_id}", status_code=status.HTTP_200_OK)
async def edit_post(post_id: int, post: schemas.Post):
    query = models.Post.select().where(post_id == models.Post.c.id)
    find_post = await database.fetch_one(query=query)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found")

    query2 = models.Post.update().where(post_id == models.Post.c.id) \
        .values(title=post.title, author=post.author, content=post.content, time_=datetime.now())
    await database.execute(query2)
    return f"Post {post_id} updated"


@router.delete("/post/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    query = models.Post.select().where(post_id == models.Post.c.id)
    find_post = await database.fetch_one(query=query)
    if not find_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} not found")

    query = models.Post.delete().where(post_id == models.Post.c.id)
    await database.execute(query)
    return {"detail": f"Post {post_id} deleted"}
