from typing import Union
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class Users(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    blogs: list[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    
    title: str
    body: str

    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config():
        orm_mode = True


class TokenData(BaseModel):
    username: Union[str, None] = None

    class Config():
        orm_mode = True