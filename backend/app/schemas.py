from pydantic import BaseModel
from typing import List, Optional

class MovieRead(BaseModel):
    """
    Schema for reading movie data from the API.
    """
    id: int
    title: str
    genres: str
    description: str

class MovieRecommendRequest(BaseModel):
    """
    Schema for recommendation request payload.
    """
    favorite_movie_id: Optional[int] = None
    genres: Optional[List[str]] = None
