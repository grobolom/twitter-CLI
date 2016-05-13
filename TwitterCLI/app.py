import os
import shutil
import json

from TwitterCLI.Screen import Screen
from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.views.TweetTabView import TweetTabView

from TwitterCLI.TweetBuilder import TweetBuilder

from TwitterCLI.reducers import RootReducer
from TwitterCLI.actions import KeyboardEventHandler
from TwitterCLI.containers import TweetWindow

from TweetSource.TweetSource import TweetSource
from TweetSource.modules import TweetFetcher
from TweetSource.utils import getTwitter

from blessed import Terminal

class TwitterClient:

    def __init__(self):
        self.screen   = Screen()
        self.terminal = Terminal()
        self.reducer  = RootReducer()
        self.keyboardEventHandler = KeyboardEventHandler()

        self.tweetWindow  = TweetWindow()
        self.timelineView = TimelineView()
        self.tweetTabView = TweetTabView()

        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)
        twitter = getTwitter(config)
        self.tweetSource = TweetSource(config, twitter)
        self.tweetFetcher = TweetFetcher(self.tweetSource)

        self.state    = self._initialState()

    def run(self):
        old_state = {}
        state = self._initialState()

        try:
            with self.terminal.fullscreen():
                with self.terminal.cbreak():
                    key = ''
                    while key != '\x03':

                        # TODO: move this somewhere where it makes sense
                        dims = shutil.get_terminal_size()

                        state['screen_width']  = dims[0]
                        state['screen_height'] = dims[1]

                        action = self._actions(key)

                        state = self.reducer.reduce(state, action)

                        if state != old_state:
                            self.render(state)

                        old_state = dict.copy(state)

                        key = self.terminal.inkey(timeout = 5)
                        if key.is_sequence:
                            key = key.name
        except KeyboardInterrupt:
            print('seeya!')
            return

    def _initialState(self):
        lists = {
            'tweets': self.tweetFetcher.getTweets(),
            'home_timeline': self.tweetFetcher.getHomeTimeline(),
        }

        for _list in self.tweetFetcher.getLists():
            lists[ _list ] = self.tweetFetcher.getListTweets(_list)

        return {
            'cursor': 0,
            'cursor_max': 200,
            'username': 'grobolom',
            'selected_list': 'tweets',
            'lists': lists,
            'last_action': 'none',
        }

    def _getTweets(self):
        return fetch_tweets()

    def _getMainList(self):
        return fetch_friend_list()

    def _actions(self, key):
        return self.keyboardEventHandler.getAction(key)

    def render(self, state):
        _w = state['screen_width']
        _h = state['screen_height']

        self.terminal.move(0, 0)
        self.screen.render(self.terminal, [
            (0, 0, self.tweetWindow.render(state)),
            (_w - 20, 0, self.tweetTabView.render(state)),
        ])
        self.terminal.move(0, 0)
