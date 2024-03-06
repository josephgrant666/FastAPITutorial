# DELETE operation using an ORM (SQLAlchemy)

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) # This decorator finds the dictionary with the given id and deletes it, sending back a status code 204
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with id: {id} does not exist")               # Raises an exception if there is no post matching the given id to delete
    post.delete(synchronize_session=False)                         # Deletes the post object
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)        # Response is sent back with status code. Data cannot be sent back here, otherwise an error occurs

