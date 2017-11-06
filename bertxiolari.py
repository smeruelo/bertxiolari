import tweepy
from bottle import request, route, run
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


@route('/search')
def search():
    screen_name = request.query.id
    # words = request.query.words
    tweets = api.user_timeline(screen_name)

    output = "<p><ul>"
    for tweet in tweets:
        output += '<li>' + tweet.text + '</li>'
    output += "</ul></p>"
    return output

run(host='localhost', port=8080, debug=True)
