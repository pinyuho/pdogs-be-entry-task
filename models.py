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
