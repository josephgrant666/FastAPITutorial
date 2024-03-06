# UPDATE operation using an ORM (SQLAlchemy)

@app.put("/posts/{id}") # This decorator finds the dictionary with the given id and deletes it, sending back a status code 204
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id) # Finds a post with a specific id
    post = post_query.first()                                       # Retrieves the post
    if post == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with id: {id} does not exist")               # Raises an exception if there is no post matching the given id to delete
    post_query.update(updated_post.dict(), synchronize_session=False)      # Updates the posts with the fields that we want 
    db.commit()                                                    # Commits the update
    return {'Data': post_query.first()}                            # Sends the update back to the user
