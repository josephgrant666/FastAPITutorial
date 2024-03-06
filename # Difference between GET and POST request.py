# Difference between GET and POST request 

# A GET request is when the user sends a request to the server, and then the server responds and gives something back to the user
# A POST request is when the user sends data to the server, and the server uses this to create something

@app.get("/") # Example of a GET request 
def root(): 
    return {"Get me some data!"}

@app.post("/") # Example of POST request 
def root():
    return {"Do something with this data!"}
