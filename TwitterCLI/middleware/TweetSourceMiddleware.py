import asyncio
class TweetSourceMiddleware:
    def __init__(self, queue):
        self.q = queue

    @asyncio.coroutine
    def handleAction(self, state, action):
        if action['name'] == 'GET_TWEETS':
            yield from self.q.put(action)
