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

        self.action_queue = []
        self.q = q

    def run(self):
        self._setupTweetFetcher()
        try:
            self.terminal.enter_fullscreen()
            self._startEventLoop()
            self.terminal.exit_fullscreen()
        except KeyboardInterrupt:
            self.terminal.exit_fullscreen()
            print(self.terminal.clear)
            print('seeya!')
        return

    def _setupTweetFetcher(self):
        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)
        twitter = getTwitter(config)
        self.tweetSource = TweetSource(config, twitter)
        self.tweetFetcher = TweetFetcher(self.tweetSource)


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
        key_action = self._actions(key)
        if key_action:
            self.q.put(key_action)

        new_state = state.copy()
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
        lists = self._getTweetLists()
        return {
            'cursor': 0,
            'cursor_max': 200,
            'username': 'grobolom',
            'selected_list': 'tweets',
            'lists': lists,
            'view': 'default',
        }

    def _getTweetLists(self):
        lists = {
            'tweets': self.tweetFetcher.getTweets(),
            'home_timeline': self.tweetFetcher.getHomeTimeline(),
        }
        for _list in self.tweetFetcher.getLists():
            lists[ 'list.' + _list ] = self.tweetFetcher.getListTweets(_list)
        return lists

    def _actions(self, key):
        return self.keyboardEventHandler.getAction(key)

    def render(self, state):
        self.layout.render(self.terminal, state)
