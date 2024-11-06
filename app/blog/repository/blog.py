from fastapi import Depends, HTTPException
from ..database import get_db
from blog import models, schemas
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(req: schemas.Blog, db: Session):
    new_blog = models.Blog(title=req.title, body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def read(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    return blog

def delete(id: int, db: Session):
    # Check if the blog exists
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    
    # If found, proceed with the deletion
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    
    return {"detail": f"Blog with id {id} deleted successfully"}

def update(id: int, req: schemas.Blog, db: Session):
    # Convert Pydantic model to dictionary
    blog_data = req.dict()  # Convert the request body to a dictionary
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")

    # Update the blog with the dictionary data
    db.query(models.Blog).filter(models.Blog.id == id).update(blog_data, synchronize_session=False)
    
    db.commit()
    db.refresh(blog)
    return blog