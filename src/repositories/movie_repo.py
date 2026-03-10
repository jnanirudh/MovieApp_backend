from repositories.db.base_repository import BaseRepository
from repositories.models.movie_model import Movie

class MovieRepo(BaseRepository):
    def get_popular_movies(self, page: int, limit: int):
        return self.session.query(Movie).offset((page - 1) * limit).limit(limit).all()

    def search_movies(self, query: str):
        return self.session.query(Movie).filter(Movie.title.ilike(f"%{query}%")).all() # '%war machine%' matches 'War Machine' -- Uses ILIKE 

    def get_movie_by_id(self, movie_id: int):
        return self.session.query(Movie).filter(Movie.id == movie_id).first()