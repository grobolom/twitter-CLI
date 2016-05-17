from TwitterCLI.TweetBuilder import TweetBuilder
import json

class TweetFetcher:
    def __init__(self, source, mongo_source):
        self.source = source
        self.mongo_source = mongo_source
        self.builder = TweetBuilder()

    def getTweets(self, since=None):
        tweets = self.mongo_source.getNewTweets(since)
        if not tweets:
            tweets = self.source.getNewTweets(since)
            self.mongo_source.saveTweets(tweets)
        return self.builder.buildTweets(tweets)

    def getHomeTimeline(self, since=None):
        tweets = self.mongo_source.getHomeTimeline(since)
        if not tweets:
            tweets = self.source.getHomeTimeline(since)
            self.mongo_source.saveHomeTimeline(tweets)
        return self.builder.buildTweets(tweets)

    def getLists(self):
        lists = self.mongo_source.getLists()
        if not lists:
            lists = self.source.getLists()
            self.mongo_source.saveLists(lists)
        return [ e['name'] for e in lists ]

    def getListTweets(self, list_name, since=None):
        tweets = self.mongo_source.getListTweets(list_name, since)
        if not tweets:
            tweets = self.source.getListTweets(list_name, since)
            self.mongo_source.saveListTweets(tweets)
        return self.builder.buildTweets(tweets)

