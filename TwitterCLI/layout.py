from TwitterCLI.Screen import Screen
from TwitterCLI.containers import TweetWindow
from TwitterCLI.containers import VerticalScrollBar
from TwitterCLI.views import TweetTab
from TwitterCLI.views import ScrollBar

def AppLayout():
    def __init__(self):
        screen = Screen()
        tweetWindow = TweetWindow()
        tweetTab = TweetTab()
        scrollBar = VerticalScrollBar()

    def render(self, terminal, state):
        _w = state['screen_width']
        _h = state['screen_height']

        terminal.move(0, 0)
        self.screen.render(terminal, [
            (0, 0, self.tweetWindow.render(state)),
            (_w - 21, 0, self.VerticalScrollBar.render(state))
            (_w - 20, 0, self.tweetTabView.render(state)),
        ])
        terminal.move(0, 0)
