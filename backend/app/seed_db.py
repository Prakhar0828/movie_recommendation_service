import json
from sqlmodel import Session
from backend.app.models import Movie
from backend.app.database import engine, create_db_and_tables
from pathlib import Path
import os

def seed_movies():
    """
    Seed the SQLite database with movies from data/seed_movies.json.
    """
    # Get the project root directory
    project_root = Path(os.getcwd())
    data_path = project_root / "data" / "seed_movies.json"
    with open(data_path, "r") as f:
        movies_data = json.load(f)
    movies = [Movie(**movie) for movie in movies_data]
    with Session(engine) as session:
        session.add_all(movies)
        session.commit()

if __name__ == "__main__":
    create_db_and_tables()
    seed_movies()
    print("Database seeded with movies!") 