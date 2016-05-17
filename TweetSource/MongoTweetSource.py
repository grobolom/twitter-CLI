class MongoTweetSource:
    def __init__(self, db):
        self.db = db

    def getNewTweets(self, since=None):
        params = {}
        if since:
            params['since'] = { '$gt': since }

        tweets = self.db.tweets.find({}, params).sort("id", -1).limit(100)
        if tweets.count(with_limit_and_skip=True):
            return tweets
        return None

    def saveTweets(self, tweets):
        self.db.tweets.insert(tweets)

    def getHomeTimeline(self, since=None):
        params = {}
        if since:
            params['since'] = { '$gt': since }

        tweets = self.db.home_timeline.find({}, params).sort("id", -1).limit(100)
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

    def saveLists(self, lists):
        self.db.list_names.insert(lists)

    def getListTweets(self, list_name, since=None):
        find = { 'slug': list_name }
        params = {}
        if since:
            params['since'] = { '$gt': since }

        tweets = self.db.lists.find(find, params).sort("id", -1).limit(100)
        if tweets.count(with_limit_and_skip=True):
            return tweets
        return None

    def saveListTweets(self, tweets):
        self.db.lists.insert(tweets)
