import os
import shutil

from TwitterCLI.Screen import Screen

from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.views.TweetTabView import TweetTabView

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
        self.tweetTabView = TweetTabView()

    def run(self):
        old_state = {}
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

                    if state != old_state:
                        self.render(dims, state)

                    old_state = dict.copy(state)

                    key = self.terminal.inkey(timeout = 5)
                    if key.is_sequence:
                        key = key.name

    def _initialState(self):
        return {
            'cursor': 0,
            'cursor_max': 200,
            'tweets': self._getTweets(),
            'username': 'grobolom',
            'available_lists': [
                'tweets',
                'home_timeline',
                'lists.friends',
            ],
            'last_action': 'none',
        }

    def _getTweets(self):
        return fetch_tweets()

    def _actions(self, key):
        key_to_action_map = {
            'k': { 'name': 'CURSOR_MOVE', 'amount' : -1 },
            'j': { 'name': 'CURSOR_MOVE', 'amount' : 1 },
            'u': { 'name': 'CURSOR_MOVE', 'amount' : -10 },
            'd': { 'name': 'CURSOR_MOVE', 'amount' : 10 },
            'KEY_TAB': { 'name': 'SWITCH_TAB', },
        }
        if key in key_to_action_map:
            return key_to_action_map[ key ]
        return { 'name': 'None' }

    def render(self, dims, state):
        self.terminal.move(0, 0)
        self.screen.render(self.terminal, [
            (0, 0, self.timelineView.render(
                state['tweets'], state['cursor'], 86, dims[1] - 1
            )),
            (dims[0] - 20, 0, self.tweetTabView.render(state)),
            (dims[0] - 20, 20, [ state['last_action'] ]),
        ])
        self.terminal.move(0, 0)
