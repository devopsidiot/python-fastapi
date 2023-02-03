from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # defaults to True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.rating)
    return {"data": "new post"}

# what we want from data - title str, content str