from sqlmodel import Session, select
from .models import Movie
from typing import List, Optional

def get_all_movies(session: Session) -> List[Movie]:
    """
    Retrieve all movies from the database.
    """
    return session.exec(select(Movie)).all()

def get_movie_by_id(session: Session, movie_id: int) -> Optional[Movie]:
    """
    Retrieve a movie by its ID.
    """
    return session.get(Movie, movie_id)

def add_movies(session: Session, movies: List[Movie]) -> None:
    """
    Add a list of movies to the database.
    """
    session.add_all(movies)
    session.commit()
