class Renderer:
    def render(self, tweet):
        lines = tweet.text.split("\n")

        first_line = [ tweet.author.rjust(15) + " " + lines[0] ]
        rest = [ " " * 16 + line for line in lines[1::]]
        return first_line + rest
