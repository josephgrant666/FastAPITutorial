# Using routers

# This is done in order to make the API code more organised, and seperate path operations into different files

# Use this in the seperated file:

from fastapi import APIRouter

router = APIRouter()

# Use this decorator on all path operations:

@router.

# Then in the main file, use this function to reference back to the file:

app.include_router(file.router)