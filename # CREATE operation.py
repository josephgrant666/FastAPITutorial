# CREATE operation

from turtle import pos
from typing import Optional
from pydantic import BaseModel
from random import randrange

class Post(BaseModel): #Pydantic models used to validate data 
    title: str
    content: str
    published: bool = True # Creates an optional field 
    rating: Optional[int] = None # Creates an optional field that doesn't store a value if the user doesn't provide it

my_posts = [{"title": "title of post one", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "i like pizza", "id": 2}]

@app.post("/posts") # Example of CREATE request without using a database 
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append()
    return {"data" : post_dict}