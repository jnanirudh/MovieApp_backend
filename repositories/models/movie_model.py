from sqlalchemy import Column, Integer, String, Text, Float, Table, ForeignKey
from repositories.db.base_repository import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False, index = True) # indexed atributes makes it easier to search
    overview = Column(Text, nullable = True) # We can have a movie without a about section
    poster_path = Column(String, nullable = True) # The string is the path to the poster image
    release_date = Column(Date, nullable = True) # Format = YYYY-MM-DD
    rating = Column(Float, nullable = True) # Rating out of 10
    original_lang = Column(String, nullable = True) # Comes in the form of "en" for english
    runtime = Column(Integer, nullable = True) # Runtime in minutes
    director = Column(String, nullable = True) 
    certification = Column(String, nullable = True) # Age rating
    
    
    
    
    