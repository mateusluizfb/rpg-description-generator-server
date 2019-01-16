from twitter import *
import os

class TwitterClient:
    @staticmethod
    def __init__(self):
        self.t_client = Twitter(auth=OAuth(os.getenv("TWITTER_TOKEN"), os.getenv("TWITTER_TOKEN_SECRET"), os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET")))

    @staticmethod
    def sendTweet(tweet):
        self.t_client.statuses.update(status=tweet)
