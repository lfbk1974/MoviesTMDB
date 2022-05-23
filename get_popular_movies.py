# Get the list of popular movies on The Movie Database. This list refreshes every day.
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

movie = Movie()
popular = movie.popular()

for p in popular:
    print(p.id)
    print(p.title)
    print(p.overview)
    print(p.poster_path)
