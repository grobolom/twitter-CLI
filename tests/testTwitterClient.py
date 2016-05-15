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
    def setUp(self):
        self.q = Queue()
        r = MockReducer()
        l = Mock()
        t = Mock()
        self.tc = TwitterClient(self.q, reducer=r, layout=l, terminal=t)

    def test_it_should_process_an_action_from_the_queue(self):
        self.q.put({ 'name': 'SWITCH_TAB' })
        state = { 'last_action': 'None' }

        actual = self.tc._handleState(None, state)
        self.assertEqual(actual, { 'last_action': 'SWITCH_TAB' })

    def test_it_should_prioritize_keyboard_actions(self):
        self.q.put({ 'name': 'SOMETHING' })
        state = { 'last_action': 'None' }

        actual = self.tc._handleState('KEY_TAB', state)
        self.assertEqual(actual, { 'last_action': 'SWITCH_TAB' })

    def test_it_should_render_the_layout(self):
        self.tc.render({ 'baconus': 'bacon' })
        self.tc.layout.render.assert_called_once_with(
            self.tc.terminal, { 'baconus': 'bacon' })
