import os
import tweepy

auth = tweepy.AppAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
api = tweepy.API(auth)


def fetch_tweets(username):
    user = api.get_user(screen_name=username)
    tweets = api.user_timeline(user_id=user.id, count=50)
    return ' '.join(list(map(lambda x: x.text, tweets)))
