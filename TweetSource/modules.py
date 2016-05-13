from TweetSource.TweetSource import TweetSource
from TwitterCLI.TweetBuilder import TweetBuilder
import json

class TweetFetcher:
    """
    a thin wrapper around the TweetSource class that handles unwrapping json
    data into the formats we want
    """
    def __init__(self, source):
        self.source = source
        self.builder = TweetBuilder()

    def getTweets(self):
        tweets = json.loads(self.source.getNewTweets())
        return self.builder.buildTweets(tweets)

    def getLists(self):
        lists = json.loads(self.source.getLists())
        return [ e['name'] for e in lists ]

    def getListTweets(self, list_name):
        tweets = json.loads(self.source.getListTweets(list_name))
        return self.builder.buildTweets(tweets)
