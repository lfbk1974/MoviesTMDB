# To retrieve movie recommendations for a given movie id
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

movie = Movie()

recommendations = movie.recommendations(movie_id=675353)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)
