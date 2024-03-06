# PUT operation 

def find_post(id):          # A function that finds a post/dictionary within an array of a certain id
    for p in my_posts:    
        if p['id'] == id:
            return p 

def find_index_post(id):    # A function that finds the id of a post/dictionary within an array
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.put("/posts/{id}")                                             # User sends a PUT request to this specific ID 
def update_post(id: int, post: Post):
    index = find_index_post(id)                                    # Finds the index
    if index == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with id: {id} does not exist")               # Raises an exception if there is no post matching the given id to update
    post_dict = post.dict()                                        # Converts the data we retrieved into a dictionary
    post_dict['id'] = id                                           # Adds the id
    my_posts[index] = post_dict                                    # Replaces the post with this index with the new post_dict
    return('Data': 'Updated post.')

# Copy the same URL as the delete operation, as it will follow the same structure and use PUT method. 
# Pass JSON body object in Postman with updated credentials 
    