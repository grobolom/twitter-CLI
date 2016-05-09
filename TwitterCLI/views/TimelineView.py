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
            author = GREEN + tweet.author.rjust(15) + END
            gutter = ' '
            text = tweet.text.ljust(self.width - 16)

            lines.append(author + gutter + text)

        return lines[0:self.height]

