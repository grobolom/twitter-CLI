class MongoTweetSource:
    def __init__(self, db):
        self.db = db

    def getNewTweets(self):
        tweets = self.db.tweets.find().sort("id", -1).limit(100)
        if tweets.count(with_limit_and_skip=True):
            return tweets
        return None

    def saveTweets(self, tweets):
        self.db.tweets.insert(tweets)

    def getHomeTimeline(self):
        tweets = self.db.home_timeline.find().sort("id", -1).limit(100)
        if tweets.count(with_limit_and_skip=True):
            return tweets
        return None

    def saveHomeTimeline(self, tweets):
        self.db.home_timeline.insert(tweets)

    def getLists(self):
        lists = self.db.list_names.find()
        if lists.count():
            return lists
        return None

    def saveLists(self, tweets):
        self.db.list_names.insert(tweets)

    def getListTweets(self):
        tweets = self.db.lists.find().sort("id", -1).limit(100)
        if tweets.count(with_limit_and_skip=True):
            return tweets
        return None

    def saveListTweets(self, tweets):
        self.db.lists.insert(tweets)
