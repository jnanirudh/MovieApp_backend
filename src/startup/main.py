from fastapi import FastAPI
from routers.movies_api import router as movies_api #locate end api points

#  Create app instance
app = FastAPI(
    title="MovieApp API",
    description="Backend API for movies reviewing app",
    version="2.0.0",
)

# Registers the router with the app instance
app.include_router(movies_api) 

@app.get("/")
def read_root():
    return {"message": "Welcome to the MovieApp API!"} # A simple get request to the root url