from repositories.movie_repo import MovieRepo
from exceptions import MovieNotFoundException

class MovieService:

    def __init__(self):
        self.movie_repo = MovieRepo()

    def get_popular_movies(self, page: int, limit: int):
        offset = (page - 1) * limit # Pagination Logic
        movies = self.repo.get_popular_movies(offset=offset, limit=limit)

        if not movies:
            NotFoundError("Movies")
        return movies

    def search_movies(self, query: str):
        results = self.repo.search_movies(query=query) 

        if not results:
            raise NotFoundError(f"Movies matching '{query}'")
        return results

    def get_movie_by_id(self, movie_id: int):
        movie = self.repo.get_movie_by_id(movie_id=movie_id) # Returns the movie object

        if not movie:
            raise NotFoundError(f"Movie with id {movie_id}") 

        return movie

# Actual thing called in the router
def get_movie_service(db: Session = Depends(get_db)):
    return MovieService(db)