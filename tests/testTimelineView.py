import unittest

from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.Tweet import Tweet

# dump colors for ease of use
from TwitterCLI.Renderer import TermAnsiColors

OKGREEN = TermAnsiColors.OKGREEN
BLUE    = TermAnsiColors.LINK
ENDC    = TermAnsiColors.ENDC
MENTION = TermAnsiColors.MENTION
HASHTAG = TermAnsiColors.HASHTAG

class TestTimelineView(unittest.TestCase):
    def test_it_should_render_tweets(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' bla ',
            OKGREEN + '           blob' + ENDC + ' haha',
        ])

    def test_it_should_not_render_lines_outside_screen(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha'),
            Tweet('bloo', 'no')
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(2, len(actual))

    def test_repeat_calls_should_print_same_lines(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        first = view.render(tweets=tweets, cursor=0, width=20, height=2)
        second = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(first, second)

    def test_it_should_chop_down_long_tweets(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'fooobaar'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' fooo',
                      '               ' +        ' baar',
        ])

    def test_it_should_display_tweets_at_the_cursor_position(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=1, width=20, height=1)
        self.assertEqual(actual, [
            OKGREEN + '           blob' + ENDC + ' haha',
        ])

    def test_it_should_treat_negative_cursor_positions_as_zero(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        zero = view.render(tweets, 0, width=20, height=1)
        negative = view.render(tweets, -1, width=20, height=1)
        self.assertEqual(zero, negative)

    def test_it_should_print_empty_lines_after_any_tweets(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'bla'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' bla ',
                      '               ' +        '     ',
        ])

    def test_it_should_right_pad_all_tweets(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'fooobaarno'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=4)
        self.assertEqual(actual, [
            OKGREEN + '           grob' + ENDC + ' fooo',
                      '               ' +        ' baar',
                      '               ' +        ' no  ',
                      '               ' +        '     ',
        ])

    def test_it_should_color_links_blue(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'foo http://something.xom'),
        ]
        actual = view.render(tweets, 0, 16 + 24, 1)
        self.assertEqual(actual, [
            OKGREEN + '           grob' \
                    + ENDC + ' foo ' + BLUE + 'http://something.xom' + ENDC,
        ])

    def test_it_should_color_mentions_yellow(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'foo @groblem'),
        ]
        actual = view.render(tweets, 0, 16 + 12, 1)
        self.assertEqual(actual, [
            OKGREEN + '           grob' \
                    + ENDC + ' foo ' + MENTION + '@groblem' + ENDC,
        ])

    def test_it_should_color_hashtags(self):
        view = TimelineView()
        tweets = [
            Tweet('grob', 'foo #groblem'),
        ]
        actual = view.render(tweets, 0, 16 + 12, 1)
        self.assertEqual(actual, [
            OKGREEN + '           grob' \
                    + ENDC + ' foo ' + HASHTAG + '#groblem' + ENDC,
        ])
