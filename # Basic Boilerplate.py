from fastapi import FastAPI

app = FastAPI() # Initialises the app

@app.get("/") # This is a decorator. This connects the function to the app. Without it, the function does nothing. 
              # The get function is the http command
              # The '\' indicates that this happens in the root address of the URL. This could be changed to specify a particular address.
def root():
    return {"message": "Hello World"}

# Commands to initiate the server:
# pip install fastapi[all] installs all fastapi dependencies to the venv
# source venv\bin\activate initiates the venv each time it is closed
# uvicorn main:app starts the server
# uvicorn main:app --reload starts the server and updates it during production
