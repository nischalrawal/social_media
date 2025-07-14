from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from random import randint


class Post (BaseModel):
    title: str
    content: str


class WritePost(BaseModel):
    title: str = Field(min_length=5)
    content: str = Field(min_length=2)


app = FastAPI()

my_post = [{"title": "title of body",
            "content": "Body of post", "id": 1}, {"title" : "Learning python", "content": " God is with me to help learn python", "id" : 2}]

def FindPost(id):
    for p in my_post:
        if p["id"] == id:
            return p
       



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your data"}


@app.post("/posts")
def post(new_post: WritePost):
    post_dict = new_post.model_dump()
    post_dict["id"] = randint(0, 1000)
    my_post.append(post_dict)
 
    return {"data" : my_post}

@app.get("/posts/{id}")
def get_id(id : int):
    post = FindPost(id)
    return{"id": post}

