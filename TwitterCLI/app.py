import shutil
import copy
from TwitterCLI.reducers import RootReducer
from TwitterCLI.actions import KeyboardEventHandler
from TwitterCLI.layout import AppLayout
from TwitterCLI.utils import Store
from blessed import Terminal
import asyncio

class TwitterClient:

    def __init__(self,
            q,
            store=Store([], {}),
            layout=AppLayout(),
            terminal=Terminal()
    ):
        self.keyboardEventHandler = KeyboardEventHandler()
        self.terminal = terminal
        self.layout = layout
        self.store = store
        self.q = q

    @asyncio.coroutine
    def run(self):
        self.terminal.enter_fullscreen()
        try:
            self._startEventLoop()
        except KeyboardInterrupt:
            pass
        finally:
            self.terminal.exit_fullscreen()
            print(self.terminal.clear)
            print('seeya!')

    def _startEventLoop(self):
        while True:
            key   = self._handleKey(self.terminal)
            state = self._handleState(key)

    def _handleKey(self, terminal):
        key = ''
        with terminal.cbreak():
            key = terminal.inkey(timeout = 0.1)

        if key.is_sequence:
            key = key.name
        return key

    def _handleState(self, key):
        """
        where we handle our state and actions. There's a bit of a complexity
        here because we have to handle both key inputs and actions passed to
        us in the queue. I've decided the best way to do this is to
        prioritize key actions over everything else, and do other updates
        only when we have time to process them - otherwise we have really
        slow visual updates when processing key input
        """
        state = self.store.getState()

        if key:
            action = self._actions(key, state)
        else:
            action = None
            try:
                action = self.q.get_nowait()
            except:
                pass

        if action:
            self.store.dispatch(action)
            new_state = self.store.getState()
            if state != new_state:
                self.render(new_state)

    def _actions(self, key, state):
        return self.keyboardEventHandler.getAction(key, state)

    def render(self, state):
        self.layout.render(self.terminal, state)
