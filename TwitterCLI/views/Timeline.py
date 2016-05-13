import textwrap
import re

import TwitterCLI.colors as colors

class Timeline:
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
        author = colors.user(tweet.author.rjust(15))
        gutter = ' ' * 16

        t = tweet.text
        w = width - 16;

        text = textwrap.wrap(t, w, break_on_hyphens=False)
        first_text = self._formatText(text[0], w)

        first = [ author + ' ' + first_text ]
        rest = [ gutter + self._formatText(line, w) for line in text[1:] ]

        return first + rest

    def _formatText(self, text, width):
        t = text.ljust(width)
        t = re.sub(r'(https?://[^\s]+)+', colors.link('\\1'), t)
        t = re.sub(r'(@[\w]+)+', colors.mention('\\1'), t)
        t = re.sub(r'(#[\w]+)+', colors.hashtag('\\1'), t)
        return t
