from sqlmodel import create_engine, Session, SQLModel
from typing import Generator

DATABASE_URL = "sqlite:///../movies.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    """
    Create database and tables if they do not exist.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """
    Dependency to get a new database session.
    """
    with Session(engine) as session:
        yield session
