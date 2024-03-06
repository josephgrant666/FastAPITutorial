# SQLAlchemy

# Install v1.4 to follow the course
# SQL doesn't know how to talk to a db. So when installed, you also need the db driver too, e.g. postgres
# Create a db file called database.py which will handle the db connection.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgesql://<username>:<password>@<ip-address/hostname>/<database-name>" # Connection string

engine = create_engine(
    SQLALCHEMY_DATABASE_URL # This is used when using a sqllite db: ,connect_args={"check_same_thread": False} 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # This is used to talk to the database

Base = declarative_base() # All of the models that we define to create our tables will use this base class

# Create a new file called models.py in order to define db tables

from .database import base # This imports the base class from the .database file
from sqlalchemy import Column, Integer, String, Boolean

class Post(Base): # Class defines the table
    __tablename__ = 'posts' # Defines the table name

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# Paste this into main.py file: models.Base.metadata.create_all(bind=engine) 
# As well as importing 'from . import models' and 'from .database import engine, SessionLocal'

# Paste this into main.py file:
# Dependency
# def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

# In the main.py file:
from sqlalchemy.orm import Session
from fastapi import Depends
# This code creates a session and passes operations 
(db: Session = Depends(get_db)):

# E.g.
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return ("status": "success")

# Take the get_db function out of the main.py file and place it into the databse.py file under the base function, then in the main.py file, import get_db from .database. After this, you can get rid of the imported 'SessionLocal' module
