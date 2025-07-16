from fastapi import Body, FastAPI, HTTPException, status

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
            "content": "Body of post", "id": 1}, {"title": "Learning python", "content": " God is with me to help learn python", "id": 2}, {"title": "Future", "content": "My life", "id": 3}]


def FindPost(id):
    for p in my_post:
        if p["id"] == id:
            return p


def deletePost(id: int):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return my_post.pop(i)
    return None


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your data"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post(new_post: WritePost):
    post_dict = new_post.model_dump()
    post_dict["id"] = randint(0, 1000)
    my_post.append(post_dict)

    return {"data": post_dict}


@app.get("/posts/{id}")
def get_id(id: int):

    post = FindPost(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id Not Found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    delete = deletePost(id)
    if not delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.put("/posts/{id}")
def update_post(id: int, received_update: WritePost):
    for i, p in enumerate(my_post):
        if p["id"] == id:
            updated_items = received_update.model_dump()
            updated_items['id'] = id
            my_post[i] = updated_items
            print(my_post)
            return updated_items
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
