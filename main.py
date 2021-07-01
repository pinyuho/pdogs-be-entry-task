from fastapi import FastAPI

import models
from database import engine
from routers import post
from routers import comment

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(comment.router)