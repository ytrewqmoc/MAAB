import requests
import random

def get_genre_id(genre_name, api_key):
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": api_key, "language": "en-US"}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        genres = response.json()["genres"]
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    print("Genre not found.")
    return None

def get_random_movie(genre_id, api_key):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {"api_key": api_key, "with_genres": genre_id, "language": "en-US", "page": random.randint(1, 10)}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
            print(f"Rating: {movie['vote_average']}/10")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch movies.")

API_KEY = "your_api_key_here"
genre_name = input("Enter a movie genre: ")
genre_id = get_genre_id(genre_name, API_KEY)

if genre_id:
    get_random_movie(genre_id, API_KEY)