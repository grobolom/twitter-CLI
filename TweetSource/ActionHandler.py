class ActionHandler:

    def __init__(self, tweetFetcher):
        self.tf = tweetFetcher

    def handleAction(self, action):
        name = action['name']

        if name == 'GET_TWEETS':
            return self._getTweets(action)

    def _getTweets(self, action):
        return self.tf.getTweets(since=action['since'])
