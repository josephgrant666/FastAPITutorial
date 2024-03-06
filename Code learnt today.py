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

# How to install PostgreSQL
# Download from the website
# Start the installer, keep the installation directory as default
# Keep all components apart from stack builder
# Create a password and keep it safe
# Default port number is 5432
# Start installation
# Use the PGAdmin GUI to manage the postgres database
# Log into PGAdmin
# Go to the servers section, and go to the Postgres databse that has already been created and log in using the PW that was created during installation
# You can create a new server by right clicking on the server tab, giving it a name, give the connection details, e.g. 'localhost'
# You can create your own postgres instance by right clicking databases -> create -> database and give the database a name
# Go to schemas -> public -> tables, right click, create -> table
# Here you can give column names, data type, Not NULL etc. 
