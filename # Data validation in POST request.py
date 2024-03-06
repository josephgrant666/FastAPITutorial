# Data validation in POST request

from typing import Optional
from pydantic import BaseModel

class Post(BaseModel): #Pydantic models used to validate data 
    title: str
    content: str
    published: bool = True # Creates an optional field 
    rating: Optional[int] = None # Creates an optional field that doesn't store a value if the user doesn't provide it

@app.post("/") # Example of POST request 
def root(post: Post): # This will validate the data being sent using the pre-defined class 
    print(post) # Will display the results. To extract the titles for example, you would add .title to the end of the post variable  
    return {"data" : "new_post"}