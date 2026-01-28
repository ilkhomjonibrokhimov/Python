import requests
import random

API_KEY = "86a47dbb"
genre = input("Enter a movie genre: ").lower()

url = "http://www.omdbapi.com/"
params = {
    "apikey": API_KEY,
    "s": genre,
    "type": "movie"
}

response = requests.get(url, params=params).json()

if "Search" in response:
    movie = random.choice(response["Search"])
    print("\nMovie Recommendation:")
    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
else:
    print("No movies found for this genre.")


