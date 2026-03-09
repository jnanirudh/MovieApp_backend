# DTO structure for movies
from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class MovieBase(BaseModel):
    id: int
    title: str
    genre: Optional[str] = None
    rating: Optional[float] = None
    poster_url: Optional[str] = None

    class Config:
        orm_mode = True 


class HomePage_List(BaseModel):
    total: int  
    page: int                         
    limit: int                         
    results: List[MovieSummary]       

    class Config:
        orm_mode = True


class SearchResult(BaseModel):
    query: str                          
    total: int                        
    results: List[MovieSummary]

    class Config:
        orm_mode = True


class MovieDetail(MovieBase):
    director: Optional[str] = None
    release_date: Optional[date] = None
    language: Optional[str] = None
    overview: Optional[str] = None

    class Config:
        orm_mode = True