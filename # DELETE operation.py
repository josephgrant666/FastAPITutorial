# DELETE operation 

def find_post(id):          # A function that finds a post/dictionary within an array of a certain id
    for p in my_posts:    
        if p['id'] == id:
            return p 

def find_index_post(id):    # A function that finds the id of a post/dictionary within an array
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) # This decorator finds the dictionary with the given id and deletes it, sending back a status code 204
def delete_post(id):
    index = find_index_post(id)                                    # Finds the index
    if index == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with id: {id} does not exist")               # Raises an exception if there is no post matching the given id to delete
    my_posts.pop(index)                                            # Removes the dictionary with the id given 
    return Response(status_code=status.HTTP_204_NO_CONTENT)        # Response is sent back with status code. Data cannot be sent back here, otherwise an error occurs

# Create new request, copy the URL and change the request to DELETE
    