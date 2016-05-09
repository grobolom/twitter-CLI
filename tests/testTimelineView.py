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

    def test_it_should_display_tweets_at_the_cursor_position(self):
        view = TimelineView(width=20, height=1)
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=1)
        self.assertEqual(actual, [
            OKGREEN + '           blob' + ENDC + ' haha',
        ])

    def test_it_should_treat_negative_cursor_positions_as_zero(self):
        view = TimelineView(width=20, height=1)
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        zero = view.render(tweets, 0)
        negative = view.render(tweets, -1)
        self.assertEqual(zero, negative)

    def test_it_should_print_empty_lines_after_any_tweets(self):
        view = TimelineView(width=20, height=2)
        tweets = [
            Tweet('grob', 'bla'),
        ]
        actual = view.render(tweets=tweets, cursor=0)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' bla ',
            '                    ',
        ])
