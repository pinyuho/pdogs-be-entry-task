from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Browse all posts
@app.get("/post", response_model=List[schemas.ShowPosts], status_code=status.HTTP_200_OK, tags=["post"])
def browse_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# Read a post by post_id
@app.get("/post/{post_id}", response_model=schemas.ShowPost, status_code=status.HTTP_200_OK, tags=["post"])
def read_post(post_id, response: Response, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id} does not exist.")
    return post

# Add a new post
@app.post("/post", status_code=status.HTTP_201_CREATED, tags=["post"])
def add_post(request: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(author=request.author, title=request.title, content=request.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Edit a post by post_id
@app.patch("/post/{post_id}", status_code=status.HTTP_202_ACCEPTED, tags=["post"])
def edit_post(post_id, request: schemas.Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    post.update({"author": request.author})
    post.update({"title": request.title})
    post.update({"content": request.content})
    db.commit()
    return "updated"

# Delete a post by post_id
@app.delete("/post/{post_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["post"])
def delete_post(post_id, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return "done"

# Add comment by post_id
@app.post("/post/{post_id}/comment", status_code=status.HTTP_201_CREATED, tags=["comment"])
def add_comment(post_id, request: schemas.Comment, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {post_id} not found")
    new_comment = models.Comment(username=request.username, content=request.content, post_id = post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment



