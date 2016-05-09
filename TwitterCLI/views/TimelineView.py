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

        return lines[cursor:self.height + cursor]

    def renderTweet(self, tweet):
        author = GREEN + tweet.author.rjust(15) + END
        gutter = ' '
        long_gutter = ' ' * 16

        text_width = self.width - 16;
        text = tweet.text[0:text_width].ljust(text_width)
        rest = tweet.text[text_width::]

        first = [author + gutter + text]

        split_points = range(0, len(rest), text_width)
        more = [long_gutter + rest[i:i+text_width] for i in split_points]

        return first + more
