# Create a post using an ORM (SQLAlchemy)

# We have to reference the model that has been created, and then specify the fields that are being passed to create a new row
# Example of a operation that creates a new entry:

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post= models.Post(title=post.title, content=post.content, published=post.published) # Creates a new entry with content for the different columns
    # A more efficient way of completing this code - better for if there are a lot of columns to extract:
    # new_post = models.Post(**post.dict()) The double star unpacks all of the fields in the models class
    db.add(new_post)        # Add the entry to the db
    db.commit()             # Commits the changes 
    db.refresh(new_post)    # Retrieves the entry that has been created and stores it into this variable
    return{"data": new_post}