from .. import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash

def create(req: schemas.Users, db: Session):
    new_user = models.User(name = req.name, email = req.email, password = Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user

def get_all(db: Session):
    users = db.query(models.User).all()
    return users