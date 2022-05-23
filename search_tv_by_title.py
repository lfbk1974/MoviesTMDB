# Search for TV shows by title.
from tmdbv3api import TMDb, TV

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

tv = TV()
show = tv.search('Breaking Bad')

for result in show:
    print(result.name)
    print(result.overview)
    print(result.values())
