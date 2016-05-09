from TwitterCLI.Renderer import Renderer

class Screen:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def render(self, tweets):
        _t = []
        n = self.columns - 16
        renderer = Renderer()
        for tweet in tweets:
            t = tweet
            line = tweet.text
            text = [line[i:i+n] for i in range(0, len(line), n)]
            text = "\n".join(text)
            t.text = text
            _t += renderer.render(t)

        for i in range(0, 10):
            print(_t[i])
