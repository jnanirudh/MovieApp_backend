from fastapi import APIRouter, Depends, Query
from services.movie_service import MovieService, get_movie_service
from contract.schemas.movie_schema import HomePageList, SearchResult, MovieDetail

router = APIRouter(prefix="/api/movies", tags= ["Movies"])

@router.get("/homepage", response_model = HomePageList) # HomePageList is the DTO defined in movie_schema file
def popular_movies(
    page: int = Query(1, ge = 1), # Default page number = 1 and page number must be >= 1 (ge)
    limit: int = Query(20, ge = 1, le = 50), # Default movie limit = 20 and limit must be >= 1 (ge) and <= 50 (le)
    service: MovieService = Depends(get_movie_service), # Depends is used to connect to service layer through get_movie_service function in the movie_service file
):
    return service.get_popular_movies(page = page, limit = limit)


@router.get("/search", response_model = SearchResult)
def search_movies(
    query: str = Query(..., min_length = 3), 
    service: MovieService = Depends(get_movie_service), 
):
    return service.search_movies(query = query)


@router.get("/movie/{movie_id}", response_model = MovieDetail)
def get_movie_by_id(
    movie_id: int,
    service: MovieService = Depends(get_movie_service), 
):
    return service.get_movie_by_id(movie_id = movie_id)

