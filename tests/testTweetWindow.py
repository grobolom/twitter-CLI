import unittest

from TwitterCLI.containers import TweetWindow
from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.Tweet import Tweet

class TestTweetWindow(unittest.TestCase):
    def setUp(self):
        self.dummy_tweet = Tweet('dummy', 'dummy_text')

    def test_it_should_render_the_timeline_view(self):
        view = TimelineView()
        state = {
            'screen_width': 80,
            'screen_height': 20,
            'cursor' : 0,
            'selected_list' : 'somelist',
            'tweets': {
                'somelist': [ self.dummy_tweet ]
            },
        }
        container = TweetWindow()
        actual = container.render(state)

        self.assertEqual(actual, view.render([ self.dummy_tweet ], 0, 60, 19))
