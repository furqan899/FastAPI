# from typing import Optional
# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()

# # ('/') In fastapi, we call this path "/"
# # and .get() is an Operation
# # @ is path operation decorator
# # the def function is a path operation function
# @app.get("/")
# async def index():
#     return {"data": "Blog List"}

# @app.get("/blog")
# def index(limit = 10, published: bool = True, sort: Optional[str] = None):
#     if published:
#         return {"data": f"{limit} published blogs"}
#     else:
#         return {"data": f"{limit} blogs"}


# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post("/blog")
# def create_blog(req: Blog):
#     return {'data': f'Blog is Created as {req.title}'}


# @app.get("/blog/unpublished")
# def about():
#     return {"data": "About Unpublished"}

# @app.get("/blogs/{id}/comments")
# def comments(id: int):
#     # fetch comments of blog with id = id from database here ... 
#     return {"data": {"1", "2"}}

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI
from app.blog import models
from app.blog.database import engine
from app.blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)