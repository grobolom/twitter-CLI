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
