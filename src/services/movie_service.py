from repositories.movie_repo import MovieRepo
from contract.exceptions.exceptions import NotFoundError
# No schema imports needed — service returns dicts, FastAPI's response_model handles conversion
from fastapi import Depends
from sqlalchemy.orm import Session
from startup.database import get_db

class MovieService:

    def __init__(self, db: Session):
        self.movie_repo = MovieRepo(db)

    def get_popular_movies(self, page: int, limit: int):
        movies = self.movie_repo.get_popular_movies(page=page, limit=limit)

        if not movies:
            raise NotFoundError("Movies")

        # Return a dict — FastAPI's response_model uses orm_mode to convert Movie objects inside 'results'
        return {"total": len(movies), "page": page, "limit": limit, "results": movies}

    def search_movies(self, query: str):
        results = self.movie_repo.search_movies(query=query)

        if not results:
            raise NotFoundError(f"Movies matching '{query}'")

        # Same pattern — dict return, FastAPI handles ORM → schema conversion
        return {"query": query, "total": len(results), "results": results}

    def get_movie_by_id(self, movie_id: int):
        movie = self.movie_repo.get_movie_by_id(movie_id=movie_id) # Returns the movie object

        if not movie:
            raise NotFoundError(f"Movie with id {movie_id}") 

        return movie

# Actual thing called in the router
def get_movie_service(db: Session = Depends(get_db)):
    return MovieService(db)