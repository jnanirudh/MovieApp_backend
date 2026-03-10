from sqlalchemy import create_engine # Creates the connection to database
from sqlalchemy.orm import sessionmaker # Used to create Session objects
from config.config import settings # gets DATABASE_URL from .env file


# The engine reads DATABASE_URL from .env
engine = create_engine(settings.DATABASE_URL)

# Creates transaction Session that will commit with db.commit()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Every route that needs the DB will call this via Depends(get_db)
def get_db():
    db = SessionLocal() # Open a new DB session for this request
    try:
        yield db # Hand the session to the route/service that requested it
    finally:
        db.close()
