from sqlmodel import Session
from .models import Movie
from typing import List, Optional

def recommend_movies(session: Session, favorite_movie_id: Optional[int] = None, genres: Optional[List[str]] = None) -> List[Movie]:
    """
    Recommend movies based on favorite_movie_id or genres.
    If favorite_movie_id is provided, recommend movies with overlapping genres, excluding the favorite movie itself.
    If genres are provided, recommend movies matching any of the genres.
    """
    query = session.query(Movie)
    if favorite_movie_id:
        favorite = session.get(Movie, favorite_movie_id)
        if not favorite:
            return []
        favorite_genres = set([g.strip() for g in favorite.genres.split(",")])
        movies = query.filter(Movie.id != favorite_movie_id).all()
        return [m for m in movies if favorite_genres.intersection([g.strip() for g in m.genres.split(",")])]
    elif genres:
        genres_set = set([g.strip() for g in genres])
        movies = query.all()
        return [m for m in movies if genres_set.intersection([g.strip() for g in m.genres.split(",")])]
    else:
        return []
