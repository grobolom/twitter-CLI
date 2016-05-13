import unittest

from TwitterCLI.views import Timeline
from TwitterCLI.Tweet import Tweet

# dump colors for ease of use
import TwitterCLI.colors as colors

class TestTimelineView(unittest.TestCase):
    def test_it_should_render_tweets(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) + ' bla ',
            colors.color('           blob', colors.USER) + ' haha',
        ])

    def test_it_should_not_render_lines_outside_screen(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha'),
            Tweet('bloo', 'no')
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(2, len(actual))

    def test_repeat_calls_should_print_same_lines(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        first = view.render(tweets=tweets, cursor=0, width=20, height=2)
        second = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(first, second)

    def test_it_should_chop_down_long_tweets(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'fooobaar'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) + ' fooo',
                         '               '               + ' baar',
        ])

    def test_it_should_display_tweets_at_the_cursor_position(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        actual = view.render(tweets=tweets, cursor=1, width=20, height=1)
        self.assertEqual(actual, [
            colors.color('           blob', colors.USER) + ' haha',
        ])

    def test_it_should_treat_negative_cursor_positions_as_zero(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
            Tweet('blob', 'haha')
        ]
        zero = view.render(tweets, 0, width=20, height=1)
        negative = view.render(tweets, -1, width=20, height=1)
        self.assertEqual(zero, negative)

    def test_it_should_print_empty_lines_after_any_tweets(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'bla'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=2)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) + ' bla ',
                      '               ' +        '     ',
        ])

    def test_it_should_right_pad_all_tweets(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'fooobaarno'),
        ]
        actual = view.render(tweets=tweets, cursor=0, width=20, height=4)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) + ' fooo',
                      '               ' +        ' baar',
                      '               ' +        ' no  ',
                      '               ' +        '     ',
        ])

    def test_it_should_color_links_blue(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'foo http://something.xom'),
        ]
        actual = view.render(tweets, 0, 16 + 24, 1)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) \
                + ' foo ' + colors.color('http://something.xom', colors.LINK),
        ])

    def test_it_should_color_mentions_yellow(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'foo @groblem'),
        ]
        actual = view.render(tweets, 0, 16 + 12, 1)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) \
                + ' foo ' + colors.color('@groblem', colors.MENTION),
        ])

    def test_it_should_color_hashtags(self):
        view = Timeline()
        tweets = [
            Tweet('grob', 'foo #groblem'),
        ]
        actual = view.render(tweets, 0, 16 + 12, 1)
        self.assertEqual(actual, [
            colors.color('           grob', colors.USER) \
                + ' foo ' + colors.color('#groblem', colors.HASHTAG),
        ])
