from TwitterCLI.Screen import Screen
from TwitterCLI.containers import TweetWindow
from TwitterCLI.containers import VerticalScrollBar

from TwitterCLI.views import TweetTab
from TwitterCLI.views import SplashScreen

class AppLayout():
    def __init__(self, screen=Screen()):
        self.screen = screen

    def render(self, terminal, state):
        _w = state['screen_width']
        _h = state['screen_height']


        selected = state['selected_list']
        view     = state['view']
        lists    = state['lists']

        terminal.move(0, 0)
        if view == 'splash' or lists == {} or selected not in lists.keys() :
            self.screen.render(terminal, self.splashView(state))
        else:
            self.screen.render(terminal, self.mainView(state))
        terminal.move(0, 0)

    def splashView(self, state):
        w = state['screen_width']
        h = state['screen_height']
        text = [
            "TwitterCLI",
            "Loading Tweets ..."
        ]
        return [
            (0, 0, SplashScreen().render(text, w, h)),
        ]

    def mainView(self, state):
        w = state['screen_width']
        h = state['screen_height']
        return [
            (0     , 0, TweetWindow().render(state)),
            (w - 21, 0, VerticalScrollBar().render(state)),
            (w - 20, 0, TweetTab().render(state)),
        ]
