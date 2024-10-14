from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# ('/') In fastapi, we call this path "/"
# and .get() is an Operation
# @ is path operation decorator
# the def function is a path operation function
@app.get("/")
async def index():
    return {"data": "Blog List"}

@app.get("/blog")
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    return published
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs"}

@app.get("/blog/unpublished")
def about():
    return {"data": "About Unpublished"}

@app.get("/blogs/{id}/comments")
def comments(id: int):
    # fetch comments of blog with id = id from database here ... 
    return {"data": {"1", "2"}}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)