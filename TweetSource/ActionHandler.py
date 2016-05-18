class ActionHandler:

    def __init__(self, tweetFetcher):
        self.tf = tweetFetcher

    def handleAction(self, action):
        name = action['name']

        if name == 'GET_TWEETS':
            return self._getTweets(action)

    def _getTweets(self, action):
        params = {}
        if 'since' in action:
            params['since'] = action['since']
        return {
            'name': 'NEW_TWEETS',
            'list': 'tweets',
            'tweets': self.tf.getTweets(**params),
        }
