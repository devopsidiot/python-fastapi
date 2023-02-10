from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True # defaults to True

class PostCreate(PostBase):
    pass
