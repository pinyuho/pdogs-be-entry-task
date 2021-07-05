from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    author: str
    content: str


class Comment(BaseModel):
    username: str
    content: str
