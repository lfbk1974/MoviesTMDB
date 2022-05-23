from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

movie = Movie()

recommendations = movie.recommendations(movie_id=675353)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)

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

username = input('Type your username: ')
password = input('Type your password: ')
USERNAME = username
PASSWORD = password

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()

print("You are logged in as %s. Your account ID is %s." % (details.username, details.id))
print("This session expires at: %s" % auth.expires_at)

movie = Movie()

s = movie.search("Gangs of New York")
first_result = s[0]
recommendations = movie.recommendations(first_result.id)

for recommendation in recommendations:
    print("Adding %s (%s) to watchlist." % (recommendation.title, recommendation.release_date))
    account.add_to_watchlist(details.id, recommendation.id, "movie")
