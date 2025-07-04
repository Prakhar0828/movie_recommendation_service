from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from typing import List
from .database import create_db_and_tables, get_session
from .models import Movie
from .crud import get_all_movies, get_movie_by_id
from .schemas import MovieRead, MovieRecommendRequest
from .recommender import recommend_movies

app = FastAPI(title="Movie Recommendation API")

@app.on_event("startup")
def on_startup():
    """
    Create database and tables on startup.
    """
    create_db_and_tables()

@app.get("/movies", response_model=List[MovieRead])
def read_movies(session: Session = Depends(get_session)):
    """
    Get a list of all movies.
    """
    return get_all_movies(session)

@app.get("/movie/{movie_id}", response_model=MovieRead)
def read_movie(movie_id: int, session: Session = Depends(get_session)):
    """
    Get details of a specific movie by ID.
    """
    movie = get_movie_by_id(session, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/recommend", response_model=List[MovieRead])
def recommend(request: MovieRecommendRequest, session: Session = Depends(get_session)):
    """
    Recommend movies based on favorite_movie_id or genres.
    """
    movies = recommend_movies(session, favorite_movie_id=request.favorite_movie_id, genres=request.genres)
    return movies
