# Search for movies by title.
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
movie = Movie()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

search = movie.search('Mad Max')

for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)
