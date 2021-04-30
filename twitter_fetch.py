from pytwitter import Api
import wcloud
from os import environ as env


def fetch_tweets(username):
    api = Api(consumer_key=env['TWITTER_CONSUMER_KEY'],
              consumer_secret=env['TWITTER_CONSUMER_SECRET'],
              access_token=env['TWITTER_ACCESS_TOKEN'],
              access_secret=env['TWITTER_ACCESS_SECRET'])

    user = api.get_user(username=username)
    tweets = api.get_timelines(user.data.id)
    return ' '.join(list(map(lambda x: x.text, tweets.data)))


def main():
    wcloud.render(fetch_tweets('kjozsa'))


if __name__ == '__main__':
    main()
