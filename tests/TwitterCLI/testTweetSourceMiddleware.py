from TwitterCLI.middleware import TweetSourceMiddleware
from queue import Queue

class TestTweetSourceMiddleware:
    def test_it_should_push_proper_actions_to_the_queue(self):
        action = {
            'name': 'GET_TWEETS',
        }
        q = Queue()
        ts = TweetSourceMiddleware(q)

        ts.handleAction({}, action)
        assert q.get(block=False) == action

    def test_it_should_return_same_state(self):
        action = {
            'name': 'GET_TWEETS',
        }
        q = Queue()
        ts = TweetSourceMiddleware(q)
        state = {
            'wut': [{ 'something': 'bad' }],
            'but': ['moo']
        }
        res = ts.handleAction(state, action)
        assert state == res
