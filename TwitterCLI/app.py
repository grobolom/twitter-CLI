import os
import shutil
import json

from TwitterCLI.TweetBuilder import TweetBuilder

from TwitterCLI.reducers import RootReducer
from TwitterCLI.actions import KeyboardEventHandler

from TwitterCLI.layout import AppLayout

from TweetSource.TweetSource import TweetSource
from TweetSource.modules import TweetFetcher
from TweetSource.utils import getTwitter

from blessed import Terminal

class TwitterClient:

    def __init__(self, q):
        self.terminal = Terminal()
        self.reducer  = RootReducer()
        self.keyboardEventHandler = KeyboardEventHandler()
        self.layout = AppLayout()

        self.q = q

    def run(self):
        try:
            self.terminal.enter_fullscreen()
            self._startEventLoop()
            self.terminal.exit_fullscreen()
        except KeyboardInterrupt:
            self.terminal.exit_fullscreen()
            print(self.terminal.clear)
            print('seeya!')
        return

    def _startEventLoop(self):
        state     = self._initialState()
        key       = ''

        self.terminal.enter_fullscreen()
        state = self._appendDims(state)
        self.render(state)
        while True:
            state = self._appendDims(state)
            state = self._handleState(key, state)
            key   = self._handleKey(self.terminal)

    def _handleKey(self, terminal):
        key = ''
        with self.terminal.cbreak():
            key = self.terminal.inkey(timeout = 0.1)
        if key.is_sequence:
            key = key.name
        return key

    def _handleState(self, key, state):
        """
        where we handle our state and actions. There's a bit of a complexity
        here because we have to handle both key inputs and actions passed to
        us in the queue. I've decided the best way to do this is to
        prioritize key actions over everything else, and do other updates
        only when we have time to process them - otherwise we have really
        slow visual updates when processing key input
        """
        new_state = state.copy()

        if key:
            action = self._actions(key)
        else:
            action = None
            try:
                action = self.q.get(block=False)
            except:
                pass

        if action:
            new_state = self.reducer.reduce(new_state, action)
            if state != new_state:
                self.render(new_state)

        return new_state

    def _appendDims(self, state):
        dims = shutil.get_terminal_size()
        state['screen_width']  = dims[0]
        state['screen_height'] = dims[1]
        return state

    def _initialState(self):
        return {
            'cursor': 0,
            'cursor_max': 200,
            'username': 'grobolom',
            'selected_list': 'tweets',
            'lists': [],
            'view': 'default',
        }

    def _actions(self, key):
        return self.keyboardEventHandler.getAction(key)

    def render(self, state):
        self.layout.render(self.terminal, state)
