class MongoTweetSource:
    def __init__(self, db):
        self.db = db

    def getNewTweets(self):
        return self.db.tweets.find().sort("id").limit(100)

    def saveTweets(self, tweets):
        self.db.tweets.insert(tweets)
