# DTO structure for movies
from pydantic import BaseModel
from datetime import date
from typing import Optional, List

# Base model inherited by
class MovieBase(BaseModel): # Every Pydantic schema must eventually trace back to BaseModel
    id: int
    title: str
    genre: Optional[str] = None
    rating: Optional[float] = None
    poster_path: Optional[str] = None  

    class Config:
        orm_mode = True 


# Home page list
class HomePageList(BaseModel):
    total: int  
    page: int                         
    limit: int                         
    results: List[MovieBase]       

    class Config:
        orm_mode = True


# Search result
class SearchResult(BaseModel):
    query: str                          
    total: int                        
    results: List[MovieBase]

    class Config:
        orm_mode = True

# For the Details page
class MovieDetail(MovieBase):
    director: Optional[str] = None
    release_date: Optional[date] = None
    language: Optional[str] = None
    overview: Optional[str] = None

    class Config:
        orm_mode = True