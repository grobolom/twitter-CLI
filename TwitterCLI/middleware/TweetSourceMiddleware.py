class TweetSourceMiddleware:
    def __init__(self, queue):
        self.q = queue

    def handleAction(self, state, action):
        if action['name'] == 'GET_TWEETS':
            self.q.put(action)
        return state
