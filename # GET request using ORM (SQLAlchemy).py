# GET request using ORM (SQLAlchemy)

@app.get("/posts/{id}") # Example of GET request with a path parameter. This will always be returned as a string. 
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first() # Searches the db using the model and looks for the first post with the id that is specified by the user in the URL
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found") # Displays a 404 error message if the ID is not found. 
        # or this could be used here: 
        # response.status_code = status.HTTP_404_NOT_FOUND
        # or 
        # return {"message: f"post with id: {id} was not found"}
        # or 
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": f"here is post {id}"}