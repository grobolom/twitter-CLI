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

