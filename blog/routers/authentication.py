from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import schemas, models, database, token
from ..hashing import Hash
router = APIRouter(
    tags=["Authentication"],
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user :
        return {"message": "Invalid username"}
    if not Hash.verify(user.password,request.password):
        return {"message": "Invalid password"}
    
    access_token = token.create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}