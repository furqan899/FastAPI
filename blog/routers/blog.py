from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from blog.repository import blog
from typing import List
router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)


@router.get('/', response_model=list[schemas.ShowBlog],  )
def read_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,  )
def create_blog(req: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(req, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog,  )
def retrieve_blog(id: int, db: Session = Depends(get_db)):
    return blog.read(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,  )
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,  )
def update_blog(id: int, req: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, req, db)