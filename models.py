from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    MetaData,
    Table,
)

metadata = MetaData()

Post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("author", String),
    Column("title", String),
    Column("content", String),
    Column("time_", DateTime),
)

Comment = Table(
    "comment",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("post_id", Integer),
    Column("username", String),
    Column("content", String),
    Column("time_", DateTime),
)


'''
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
'''