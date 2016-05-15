import unittest
import time
from mock import MagicMock as Mock
from queue import Queue
from TwitterCLI.app import TwitterClient

class MockReducer:
    def reduce(self, state, action):
        s = state
        s['last_action'] = action['name']
        return s

class TestTwitterClient(unittest.TestCase):
    def test_it_should_process_an_action_from_the_queue(self):
        q = Queue()
        q.put({ 'name': 'SWITCH_TAB' })

        r = MockReducer()
        l = Mock()
        t = Mock()
        tc = TwitterClient(q, reducer=r, layout=l, terminal=t)
        tc.render = Mock()

        state = { 'last_action': 'None' }
        actual = tc._handleState(None, state)
        self.assertEqual(actual, { 'last_action': 'SWITCH_TAB' })

    def test_it_should_prioritize_keyboard_actions(self):
        q = Queue()
        q.put({ 'name': 'SOMETHING' })

        r = MockReducer()
        l = Mock()
        t = Mock()
        tc = TwitterClient(q, reducer=r, layout=l, terminal=t)
        tc.render = Mock()

        state = { 'last_action': 'None' }
        actual = tc._handleState('KEY_TAB', state)
        self.assertEqual(actual, { 'last_action': 'SWITCH_TAB' })
