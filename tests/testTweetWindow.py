import unittest

from TwitterCLI.containers import TweetWindow
from TwitterCLI.views import Timeline
from TwitterCLI.Tweet import Tweet

class TestTweetWindow(unittest.TestCase):
    def setUp(self):
        self.dummy_tweet = Tweet('dummy', 'dummy_text')

    def test_it_should_render_the_timeline_view(self):
        view = Timeline()
        state = {
            'screen_width': 80,
            'screen_height': 20,
            'selected_list' : 'somelist',
            'lists': {
                'somelist': {
                    'tweets': [ self.dummy_tweet ],
                    'cursor': 0,
                    'cursor_max': 20,
                }
            },
        }
        container = TweetWindow()
        actual = container.render(state)

        self.assertEqual(actual, view.render([ self.dummy_tweet ], 0, 58, 19))
