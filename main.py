from fastapi import FastAPI

from models import metadata
from database import engine, database
from routers import post
from routers import comment

metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

app.include_router(post.router)
app.include_router(comment.router)
