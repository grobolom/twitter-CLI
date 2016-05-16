import unittest

from TwitterCLI.views import TweetTab
from TwitterCLI.Tweet import Tweet

import TwitterCLI.colors as colors

class TestTweetTabView(unittest.TestCase):
    def test_it_should_display_a_title_and_username(self):
        v = TweetTab()
        state = {
            'username': 'grobolom',
        }
        actual = v.render(state)
        self.assertEqual(actual[0:2], [
            colors.title('TwitterCLI          '),
            colors.user( '@grobolom           '),
        ])

    def test_it_should_render_all_tabs(self):
        v = TweetTab()
        state = {
            'username': 'grobolom',
            'lists': {
                'tweets' : [],
                'home_timeline' : [],
                }
        }
        actual = v.render(state)
        self.assertEqual(actual, [
            colors.title('TwitterCLI          '),
            colors.user( '@grobolom           '),
            '                    ',
            '  Home Timeline     ',
            '  Tweets            ',
        ])

    def test_it_should_render_lists(self):
        v = TweetTab()
        state = {
            'username': 'grobolom',
            'lists': {
                'tweets' : [],
                'home_timeline' : [],
                'list.friends' : [],
                'list.other_list' : [],
            }
        }
        actual = v.render(state)
        self.assertEqual(actual, [
            colors.title('TwitterCLI          '),
            colors.user( '@grobolom           '),
            '                    ',
            '  Home Timeline     ',
            '  Tweets            ',
            '    Friends         ',
            '    Other List      ',
        ])

