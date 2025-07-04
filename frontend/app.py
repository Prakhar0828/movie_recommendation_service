import streamlit as st
import requests
from typing import List, Dict

# -----------------------------
# Backend API configuration
# -----------------------------
API_URL = "https://movie-recommendation-service-8qiw.onrender.com"  # Change if backend runs elsewhere

# -----------------------------
# Helper functions for API calls
# -----------------------------
def fetch_movies() -> List[Dict]:
    """Fetch all movies from the backend API."""
    try:
        response = requests.get(f"{API_URL}/movies")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch movies: {e}")
        return []

def fetch_genres(movies: List[Dict]) -> List[str]:
    """Extract unique genres from the list of movies."""
    genres = set()
    for movie in movies:
        genres.update([g.strip() for g in movie["genres"].split(",")])
    return sorted(genres)

def fetch_recommendations(favorite_movie_id: int = None, genres: List[str] = None) -> List[Dict]:
    """Fetch recommended movies from the backend API."""
    payload = {}
    if favorite_movie_id:
        payload["favorite_movie_id"] = favorite_movie_id
    if genres:
        payload["genres"] = genres
    try:
        response = requests.post(f"{API_URL}/recommend", json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Failed to fetch recommendations: {e}")
        return []

def fetch_movie_by_id(movie_id: int, movies: List[Dict]) -> Dict:
    """Return a movie dict by its ID from the local list."""
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {}

# -----------------------------
# Navigation callback functions
# -----------------------------
def go_to_input():
    st.session_state.page = "input"

def go_to_landing():
    st.session_state.page = "landing"

def go_to_recommend(movie_options, favorite_movie, selected_genres):
    st.session_state.page = "recommend"
    st.session_state.favorite_movie_id = movie_options.get(favorite_movie) if favorite_movie != "None" else None
    st.session_state.selected_genres = selected_genres

def go_to_input_from_recommend():
    st.session_state.page = "input"

# -----------------------------
# Streamlit UI
# -----------------------------
def landing_page():
    """Display the landing page."""
    st.title("🎬 Movie Recommendation App")
    st.write("Welcome! Get personalized movie recommendations in seconds.")
    st.button("Get Movie Recommendations", on_click=go_to_input)

def input_page():
    """Display the input page for user preferences."""
    st.header("Tell us your movie taste!")
    st.write("Choose a favorite movie or select genres you like.")
    # Fetch movies from backend
    movies = fetch_movies()
    if not movies:
        st.warning("No movies available.")
        return
    movie_options = {m["title"]: m["id"] for m in movies}
    favorite_movie = st.selectbox("Pick a favorite movie (optional):", ["None"] + list(movie_options.keys()), key="favorite_movie_select")
    # Genre selection
    all_genres = fetch_genres(movies)
    selected_genres = st.multiselect("Or select genres you like:", all_genres, key="genre_multiselect")
    # Submit button
    st.button(
        "Get Recommendations",
        on_click=go_to_recommend,
        args=(movie_options, favorite_movie, selected_genres)
    )
    st.button("Back", on_click=go_to_landing)

def recommendation_page():
    """Display the recommended movies."""
    st.header("Recommended Movies")
    fav_id = st.session_state.get("favorite_movie_id")
    genres = st.session_state.get("selected_genres", [])
    recommendations = fetch_recommendations(favorite_movie_id=fav_id, genres=genres)
    if not recommendations:
        st.info("No recommendations found. Try different options.")
    else:
        for movie in recommendations:
            st.subheader(movie["title"])
            st.write(f"**Genres:** {movie['genres']}")
            st.write(movie["description"])
            st.markdown("---")
    st.button("Try Again", on_click=go_to_input_from_recommend)

# -----------------------------
# Main app logic
# -----------------------------
def main():
    """Main function to control page navigation."""
    if "page" not in st.session_state:
        st.session_state.page = "landing"
    if st.session_state.page == "landing":
        landing_page()
    elif st.session_state.page == "input":
        input_page()
    elif st.session_state.page == "recommend":
        recommendation_page()

if __name__ == "__main__":
    main()
