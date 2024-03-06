# Retrieve one individual entry 

from typing import Optional
from urllib import response
from pydantic import BaseModel
from random import randrange

class Post(BaseModel): #Pydantic models used to validate data 
    title: str
    content: str
    published: bool = True # Creates an optional field 
    rating: Optional[int] = None # Creates an optional field that doesn't store a value if the user doesn't provide it

my_posts = [{"title": "title of post one", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "i like pizza", "id": 2}]

def find_post(id):
    for p in my_posts: 
        if p ["id"] == id:
            return p

@app.get("/posts/{id}") # Example of GET request with a path parameter. This will always be returned as a string. 
def get_post(id: int):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found") # Displays a 404 error message if the ID is not found. 
        # or this could be used here: 
        # response.status_code = status.HTTP_404_NOT_FOUND
        # or 
        # return {"message: f"post with id: {id} was not found"}
        # or 
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": f"here is post {id}"}