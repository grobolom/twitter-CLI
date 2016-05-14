from TwitterCLI.Screen import Screen
from TwitterCLI.containers import TweetWindow
from TwitterCLI.containers import VerticalScrollBar

from TwitterCLI.views import TweetTab
from TwitterCLI.views import ScrollBar
from TwitterCLI.views import SplashScreen

class AppLayout():
    def __init__(self):
        self.screen = Screen()

    def render(self, terminal, state):
        _w = state['screen_width']
        _h = state['screen_height']

        terminal.move(0, 0)
        if state['view'] == 'splash':
            self.screen.render(terminal, splashView(state))
        else:
            self.screen.render(terminal, mainView(state))
        terminal.move(0, 0)

def splashView(state):
    w = state['screen_width']
    h = state['screen_height']
    text = [
        "TwitterCLI",
        "Loading Tweets ..."
    ]
    return [
        (0, 0, SplashScreen().render(text, w, h)),
    ]

def mainView(state):
    w = state['screen_width']
    h = state['screen_height']
    return [
        (0     , 0, TweetWindow().render(state)),
        (w - 21, 0, ScrollBar().render(state)),
        (w - 20, 0, TweetTab().render(state)),
    ]
