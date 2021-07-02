from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    content = Column(String)
    time_ = Column(DateTime)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer)
    username = Column(String)
    content = Column(String)
    time_ = Column(DateTime)