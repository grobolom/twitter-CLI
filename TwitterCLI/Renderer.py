class TermAnsiColors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    LINKBLUE = '\034[40m'

class Renderer:
    def render(self, tweet):
        lines = tweet.text.split("\n")

        author_part = TermAnsiColors.OKGREEN + \
            tweet.author.rjust(15) + \
            " " + \
            TermAnsiColors.ENDC
        first_line = [ author_part + lines[0] ]
        rest = [ " " * 16 + line for line in lines[1::]]
        return first_line + rest
