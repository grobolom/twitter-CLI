class TwitterWrapper:
    def __init__(self, config, twitter):
        self.config = config
        self.twitter = twitter

    def getNewTweets(self, since=None):
        params = {}
        if since:
            params['since'] = since

        return self.twitter.statuses.user_timeline(
            screen_name = self.config['user'],
            include_rts = False,
            count = 500,
            **params
        )

    def getLists(self):
        return self.twitter.lists.list(
            screen_name = self.config['user']
        )

    def getListTweets(self, list_name, since=None):
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

    def getHomeTimeline(self):
        return self.twitter.statuses.home_timeline(
            count = 200
        )
