from TwitterCLI.TweetBuilder import TweetBuilder
import json

class TweetFetcher:
    def __init__(self, source, mongo_source):
        self.source = source
        self.mongo_source = mongo_source
        self.builder = TweetBuilder()

    def getTweets(self):
        tweets = self.mongo_source.getNewTweets()
        if not tweets:
            tweets = self.source.getNewTweets()
            self.mongo_source.saveTweets(tweets)
        return self.builder.buildTweets(tweets)

    def getHomeTimeline(self):
        tweets = self.mongo_source.getHomeTimeline()
        if not tweets:
            tweets = self.source.getHomeTimeline()
            self.mongo_source.saveHomeTimeline(tweets)
        return self.builder.buildTweets(tweets)

    def getLists(self):
        lists = self.mongo_source.getLists()
        if not lists:
            lists = self.source.getLists()
            self.mongo_source.saveLists(lists)
        return [ e['name'] for e in lists ]

    def getListTweets(self, list_name):
        tweets = self.mongo_source.getListTweets(list_name)
        if not tweets:
            tweets = self.source.getListTweets(list_name)
            self.mongo_source.saveListTweets(tweets)
        return self.builder.buildTweets(tweets)

