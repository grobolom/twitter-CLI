import unittest

from TwitterCLI.views.TweetTabView import TweetTabView
from TwitterCLI.Tweet import Tweet

class TestTweetTabView(unittest.TestCase):
    def test_it_should_display_a_title_and_username(self):
        v = TweetTabView()
        state = {
            'username': 'grobolom',
        }
        actual = v.render(state)
        self.assertEqual(actual[0:2], [
            'TwitterCLI          ',
            '@grobolom           ',
        ])
