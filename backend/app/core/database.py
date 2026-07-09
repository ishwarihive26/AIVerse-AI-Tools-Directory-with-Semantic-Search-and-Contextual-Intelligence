"""
This file sets up the connection between FastAPI and MySQL using
SQLAlchemy. Every model (Tool, Category, User, etc.) will import
`Base` from here, and every route that talks to the database will
use `get_db` to get a database session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

# The engine manages the actual connection pool to MySQL
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Each request gets its own session (like a "conversation" with the DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All models will inherit from this Base class
Base = declarative_base()


def get_db():
    """
    FastAPI dependency. Opens a DB session for a request,
    and always closes it afterward - even if an error happens.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
