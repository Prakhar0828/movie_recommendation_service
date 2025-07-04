# Movie Recommendation App

## Project Directory Structure

```
movie_recommendation_app/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI entry point
│   │   ├── models.py            # SQLModel/SQLAlchemy models
│   │   ├── database.py          # DB connection and setup
│   │   ├── crud.py              # DB operations (create/read/update/delete)
│   │   ├── schemas.py           # Pydantic schemas (if needed)
│   │   └── recommender.py       # Recommendation logic
│   └── requirements.txt         # Backend dependencies
│
├── frontend/
│   ├── app.py                   # Streamlit entry point
│   └── requirements.txt         # Frontend dependencies
│
├── data/
│   └── seed_movies.json         # Initial dummy movie data (for DB seeding)
│
├── movies.db                    # SQLite database file (created at runtime)
│
├── README.md
└── .gitignore
```

---

- **backend/app/**: FastAPI backend code.
- **frontend/**: Streamlit frontend code.
- **data/seed_movies.json**: Dummy movie data for seeding the database.
- **movies.db**: SQLite database file (auto-created at runtime).
- **requirements.txt**: Separate for backend and frontend.
- **README.md**: Project overview and setup instructions.
- **.gitignore**: Ignore files like `movies.db`, `__pycache__`, etc.
