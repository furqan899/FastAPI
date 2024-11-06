from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from app.blog.repository import user
router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(req: schemas.Users, db: Session = Depends(get_db)):

    return user.create(req, db)

@router.get('/', response_model=list[schemas.ShowUser], )
def read_user(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser )
def retrieve_user(id: int, db: Session = Depends(get_db)):
    return user.read(id, db)