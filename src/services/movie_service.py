from repositories.movie_repo import MovieRepo
from utils.exceptions import NotFoundError
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

class MovieService:

    def __init__(self, db: Session):
        self.movie_repo = MovieRepo(db)

    def get_popular_movies(self, page: int, limit: int):
        movies = self.movie_repo.get_popular_movies(page=page, limit=limit)

        if not movies:
            raise NotFoundError("Movies")
        return movies

    def search_movies(self, query: str):
        results = self.movie_repo.search_movies(query=query) 

        if not results:
            raise NotFoundError(f"Movies matching '{query}'")
        return results

    def get_movie_by_id(self, movie_id: int):
        movie = self.movie_repo.get_movie_by_id(movie_id=movie_id) # Returns the movie object

        if not movie:
            raise NotFoundError(f"Movie with id {movie_id}") 

        return movie

# Actual thing called in the router
def get_movie_service(db: Session = Depends(get_db)):
    return MovieService(db)