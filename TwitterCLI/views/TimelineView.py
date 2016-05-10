import textwrap
import re

from TwitterCLI.Renderer import TermAnsiColors

GREEN = TermAnsiColors.OKGREEN
END   = TermAnsiColors.ENDC
BLUE  = TermAnsiColors.LINKBLUE

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
        gutter = ' ' * 16

        t = tweet.text
        w = width - 16;

        text = textwrap.wrap(t, w, break_on_hyphens=False)
        first_text = self._formatText(text[0], w)

        first = [ author + ' ' + first_text ]
        rest = [ gutter + self._formatText(line, w) for line in text[1:] ]

        return first + rest

    def _formatText(self, text, width):
        j = text.ljust(width)
        colored = re.sub(r'(https?://[^\s]+)+', BLUE + '\\1' + END, j)
        return colored
