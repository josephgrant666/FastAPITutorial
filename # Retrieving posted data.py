# Retrieving posted data

from fastapi.params import body 

@app.post("/") # Example of POST request 
def root(payload: dict = Body(...)): # This will find instances of data in the body of the text that has been posted, convert it as a dictionary, and store it as the variable 'payload'.
    print(payload) # Will display the results 
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}
