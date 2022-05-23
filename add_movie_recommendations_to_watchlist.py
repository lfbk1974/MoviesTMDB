# Login to your account and add some movie recommendations to your TMDb watchlist.
from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
with open('key.txt') as f:
    tmdb_key_from_file = f.read()
tmdb.api_key = tmdb_key_from_file

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

movie_to_find_recommendations = input('Movie to find recommendations: ')
s = movie.search(movie_to_find_recommendations)
first_result = s[0]
recommendations = movie.recommendations(first_result.id)

for recommendation in recommendations:
    print("Adding %s (%s) to watchlist." % (recommendation.title, recommendation.release_date))
    account.add_to_watchlist(details.id, recommendation.id, "movie")
