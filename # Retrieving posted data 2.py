# Retrieving data 

from typing import Optional
from pydantic import BaseModel

class Post(BaseModel): #Pydantic models used to validate data 
    title: str
    content: str
    published: bool = True # Creates an optional field 
    rating: Optional[int] = None # Creates an optional field that doesn't store a value if the user doesn't provide it

my_posts = [{"title": "title of post one", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "i like pizza", "id": 2}]

@app.post("/posts") # Example of POST request 
def get_posts():
    return {"data" : my_posts}