import os
import shutil

from TwitterCLI.Screen import Screen
from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.fetch_tweets import fetch_tweets
from TwitterCLI.TweetBuilder import TweetBuilder
from TwitterCLI.reducers import RootReducer

from blessed import Terminal

class TwitterClient:

    def __init__(self):
        self.screen   = Screen()
        self.terminal = Terminal()
        self.reducer  = RootReducer()
        self.state    = self._initialState()

        self.timelineView = TimelineView()

    def run(self):
        state = self._initialState()
        with self.terminal.fullscreen():
            with self.terminal.cbreak():
                key = ''
                while key != '\x03':
                    if key == 'x':
                        os.system('clear')
                    dims = shutil.get_terminal_size()
                    action = self._actions(key)
                    state = self.reducer.reduce(state, action)
                    self.render(dims, state)
                    key = self.terminal.inkey(timeout = 5)

    def _initialState(self):
        return {
            'cursor': 0,
            'cursor_max': '200',
            'tweets': self._getTweets(),
        }

    def _getTweets(self):
        return fetch_tweets()

    def _actions(self, key):
        key_to_action_map = {
            'k': 'CURSOR_UP',
            'j': 'CURSOR_DOWN',
        }
        if key in key_to_action_map:
            return key_to_action_map[ key ]
        return None

    def render(self, dims, state):
        self.terminal.move(0, 0)
        self.screen.render(self.terminal, [
            (0, 0, self.timelineView.render(
                state['tweets'], state['cursor'], 86, dims[1] - 1
            )),
            (dims[0] - 19, 0, [ ' ' + e.ljust(19) for e in [
                'TwitterCLI',
                '@grobolom',
                'Friends',
                'tweets: ' + str(len(state['tweets'])),
                'index : ' + str(state['cursor']),
                'max   : ' + str(state['cursor_max']),
                'x     : ' + str(dims[0]),
                'y     : ' + str(dims[1]),
            ]] + [' ' * 19])
        ])
        self.terminal.move(0, 0)
