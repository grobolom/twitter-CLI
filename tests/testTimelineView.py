import unittest
from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.Tweet import Tweet

# dump colors for ease of use
from TwitterCLI.Renderer import TermAnsiColors

OKGREEN = TermAnsiColors.OKGREEN
ENDC = TermAnsiColors.ENDC

class TestRenderer(unittest.TestCase):
    def test_it_should_render_tweets(self):
        view = TimelineView(width=20, height=2)
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=0)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' bla ',
            OKGREEN + '           blob' + ENDC + ' haha',
        ])

    def test_it_should_not_render_lines_outside_screen(self):
        view = TimelineView(width=20, height=2)
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha'),
            Tweet('bloo', 'no')
        ]
        actual = view.render(tweets=tweets, cursor=0)
        self.assertEqual(2, len(actual))

    def test_repeat_calls_should_print_same_lines(self):
        view = TimelineView(width=20, height=2)
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        first = view.render(tweets=tweets, cursor=0)
        second = view.render(tweets=tweets, cursor=0)
        self.assertEqual(first, second)

    def test_it_should_chop_down_long_tweets(self):
        view = TimelineView(width=20, height=2)
        tweets = [
            Tweet('grob', 'fooobaar'),
        ]
        actual = view.render(tweets=tweets, cursor=0)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' fooo',
            '                baar',
        ])
