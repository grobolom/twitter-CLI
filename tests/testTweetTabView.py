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

    def test_it_should_render_all_tabs(self):
        v = TweetTabView()
        state = {
            'username': 'grobolom',
            'available_lists': [
                'tweets',
                'home_timeline',
            ]
        }
        actual = v.render(state)
        self.assertEqual(actual, [
            'TwitterCLI          ',
            '@grobolom           ',
            '                    ',
            '  Tweets            ',
            '  Home Timeline     ',
        ])

    def test_it_should_render_lists(self):
        v = TweetTabView()
        state = {
            'username': 'grobolom',
            'available_lists': [
                'tweets',
                'home_timeline',
                'list.friends',
                'list.other_list',
            ]
        }
        actual = v.render(state)
        self.assertEqual(actual, [
            'TwitterCLI          ',
            '@grobolom           ',
            '                    ',
            '  Tweets            ',
            '  Home Timeline     ',
            '                    ',
            '  Lists:            ',
            '    Friends         ',
            '    Other List      ',
        ])

