from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    author: str
    content: str

class Comment(BaseModel):
    username: str
    content: str

# Show Functions
class ShowPost(BaseModel):
    title: str
    author: str
    content: str
    # comments: List
    class Config():
        orm_mode = True

class ShowPosts(BaseModel):
    id: int
    title: str
    author: str
    content: str
    class Config():
        orm_mode = True


class ShowComment(BaseModel): # For reading a post
    username: str
    content: str
    # a_post: Post
    class Config():
        orm_mode = True

class ShowComments(BaseModel):
    username: str
    content: str
    class Config():
        orm_mode = True


