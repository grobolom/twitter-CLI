class TwitterHandler:
    def __init__(self, config, cache=None):
        self.config = config
        self.cache = cache

    def getTweets(self):
        tweets = []
        if self.cache:
            tweets = self.cache.getTweets()
        return tweets
        pass
