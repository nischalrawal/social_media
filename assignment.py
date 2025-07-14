from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class write_blog(BaseModel):
    author: str = Field(min_length=2)
    age: int = Field(gt=2)
    interest: str = Field(min_length=2)
    rating: Optional[int] = None


# Homepage
@app.get("/")
def root():
    return {"message": "Welcome to vlog post"}


@app.get('/readblog')
def read_blog():
    return {"Data Fetched Successfully"}

# Create post


@app.post("/writeblog")
def write_vlog(new_blog: write_blog):
    print(new_blog)
    print(new_blog.model_dump())
    
    return {"Vlog created successfully"}
