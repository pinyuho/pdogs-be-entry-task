from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Post(BaseModel):
    id: int
    username: str
    title: str
    content: str
    update_time: Optional[datetime]
    # is_deleted: Optional[bool]
    pass

class Comment(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool]
    pass


@app.post("/post")
def create_post(post: Post):
    return {"data": f"Post is created with title {post.title}"}

@app.get("/post")
def index(limit=20, published: bool=True, sort: Optional[str] = None):
    if published:
        return {"data": f"published post_list {limit}"}
    else:
        return {"data": f"all post_list {limit}"}


@app.get("/post/unpublished")
def unpublished():
    return {"data": "all unpublished posts"}


@app.get("/post/{post_id}")
def show(post_id: int):
    return {"data": post_id}


@app.get("/post/{post_id}/comment")
def comments(post_id):
    return {"data": {"1", "2"}}

