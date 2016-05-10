import textwrap

from TwitterCLI.Renderer import TermAnsiColors

GREEN = TermAnsiColors.OKGREEN
END = TermAnsiColors.ENDC

class TimelineView:
    def render(self, tweets, cursor, width, height):
        lines = []
        for tweet in tweets:
            lines += self._renderTweet(tweet, width)

        _cursor = cursor
        if _cursor < 0:
            _cursor = 0

        tweet_lines = lines[_cursor:height + _cursor]

        difference = height - len(tweet_lines)
        if difference > 0:
            tweet_lines += [' ' * width for i in range(0, difference)]

        return tweet_lines

    def _renderTweet(self, tweet, width):
        author = GREEN + tweet.author.rjust(15) + END
        gutter = ' '
        long_gutter = ' ' * 16
        text_width = width - 16;

        text = textwrap.wrap(tweet.text, text_width, break_on_hyphens=False)

        first_text = text[0].ljust(text_width)

        first = [ author + gutter + first_text ]
        rest = [ long_gutter + line.ljust(text_width) for line in text[1:] ]

        return first + rest
