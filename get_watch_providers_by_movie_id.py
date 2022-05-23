import requests

from tmdbv3api.tmdb import TMDb

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

movie_id = '260513'
api_url = "https://api.themoviedb.org/3/movie/" + movie_id + "/watch/providers?api_key=" + tmdb.api_key + "&locale=BR"
response = requests.get(api_url)
response.json()
print(response.json())