class TweetSource:
    def __init__(self, config, twitter, mongodb):
        self.config = config
        self.twitter = twitter

    def _getNewTweets(self, since=None):
        params = {}
        if since:
            params['since'] = since

        return self.twitter.statuses.user_timeline(
            screen_name = self.config['user'],
            include_rts = False,
            **params
        )
