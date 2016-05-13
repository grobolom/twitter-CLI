from TwitterCLI.Screen import Screen
from TwitterCLI.containers import TweetWindow
from TwitterCLI.containers import VerticalScrollBar
from TwitterCLI.views import TweetTab
from TwitterCLI.views import ScrollBar

class AppLayout():
    def __init__(self):
        self.screen = Screen()
        self.tweetWindow = TweetWindow()
        self.tweetTab = TweetTab()
        self.scrollBar = VerticalScrollBar()

    def render(self, terminal, state):
        _w = state['screen_width']
        _h = state['screen_height']

        terminal.move(0, 0)
        self.screen.render(terminal, [
            (0, 0, self.tweetWindow.render(state)),
            (_w - 21, 0, self.scrollBar.render(state)),
            (_w - 20, 0, self.tweetTab.render(state)),
        ])
        terminal.move(0, 0)
