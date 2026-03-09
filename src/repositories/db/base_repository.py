from sqlalchemy.orm import Session, DeclarativeBase

# All SQLAlchemy models inherit from this Base class (it creates the table registry)
class Base(DeclarativeBase):
    pass

# BaseRepository holds the DB session and is the parent for all repo classes
class BaseRepository:
    def __init__(self, db: Session):
        self.session = db 