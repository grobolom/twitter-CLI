from TwitterCLI.Renderer import TermAnsiColors

GREEN = TermAnsiColors.OKGREEN
END = TermAnsiColors.ENDC

class TimelineView:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render(self, tweets, cursor):
        lines = []
        for tweet in tweets:
            lines += self.renderTweet(tweet)

        _cursor = cursor
        if _cursor < 0:
            _cursor = 0

        tweet_lines = lines[_cursor:self.height + _cursor]

        difference = self.height - len(tweet_lines)
        if difference > 0:
            tweet_lines += [' ' * self.width for i in range(0, difference)]

        return tweet_lines

    def renderTweet(self, tweet):
        author = GREEN + tweet.author.rjust(15) + END
        gutter = ' '
        long_gutter = ' ' * 16

        text_width = self.width - 16;
        text = tweet.text[0:text_width].ljust(text_width)
        rest = tweet.text[text_width::]

        first = [author + gutter + text]

        more = []
        split_points = range(0, len(rest), text_width)
        for i in split_points:
            line = long_gutter + rest[i:i + text_width].ljust(text_width)
            more += [ line ]

        return first + more
