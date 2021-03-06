from tmdbv3api import TMDb, Movie

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

m = movie.details(343611)

print(m.title)
print(m.overview)
print(m.popularity)
