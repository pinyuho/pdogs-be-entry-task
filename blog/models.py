from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    content = Column(String)

    comments = relationship("Comment", back_populates="a_post")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    username = Column(String)
    content = Column(String)

    a_post = relationship("Post", back_populates="comments")




