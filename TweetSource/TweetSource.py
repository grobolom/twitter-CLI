from TwitterCLI.TweetBuilder import TweetBuilder

class TweetSource:
    def __init__(self, config, twitter):
        self.config = config
        self.twitter = twitter
        self.builder = TweetBuilder()

    def get_new_tweets(self):
        tweets = self._getNewTweets()
        return self.builder.buildTweets(tweets)

    def get_list_tweets(self, list_name):
        tweets = self._getListTweets(list_name)
        return self.builder.buildTweets(tweets)

    def _getNewTweets(self, since=None):
        params = {}
        if since:
            params['since'] = since

        return self.twitter.statuses.user_timeline(
            screen_name = self.config['user'],
            include_rts = False,
            count = 500,
            **params
        )

    def _getListTweets(self, list_name, since=None):
        params = {}
        if since:
            params['since'] = since

        return self.twitter.lists.statuses(
            slug=list_name,
            owner_screen_name = self.config['user'],
            include_rts = False,
            count = 500,
            **params
        )
