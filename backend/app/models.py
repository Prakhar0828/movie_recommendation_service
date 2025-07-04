from sqlmodel import SQLModel, Field

class Movie(SQLModel, table=True):
    """
    Movie model for storing movie information in the SQLite database.
    """
    id: int = Field(default=None, primary_key=True)
    title: str
    genres: str  # Comma-separated genres, e.g., "Action,Comedy"
    description: str
