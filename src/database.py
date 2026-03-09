from sqlalchemy import create_engine          # Creates the connection to your database
from sqlalchemy.orm import sessionmaker        # Factory that creates Session objects
from config.config import settings            # Pulls DATABASE_URL from your .env file

# Step 1: Create the engine — the actual connection to your database
# The engine reads DATABASE_URL from .env, e.g. "postgresql://user:pass@localhost/movieapp"
engine = create_engine(settings.DATABASE_URL)

# Step 2: Create a session factory
# autocommit=False → changes aren't saved until you explicitly call db.commit()
# autoflush=False  → SQLAlchemy won't auto-send pending changes to DB mid-session
# bind=engine      → ties every session to the database engine above
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Step 3: get_db — a generator function used by FastAPI's dependency injection (Depends)
# Every route that needs the DB will call this via Depends(get_db)
def get_db():
    db = SessionLocal()   # Open a new DB session for this request
    try:
        yield db          # Hand the session to the route/service that requested it
    finally:
        db.close()        # Always close the session when the request is done
