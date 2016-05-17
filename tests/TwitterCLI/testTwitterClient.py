import unittest
import time

from mock import MagicMock as Mock, patch
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

    def test_it_should_not_render_when_state_is_the_same(self):
        state = {}
        actual = self.tc._handleState(None, state)
        self.tc.layout.render.assert_not_called()

    def test_it_should_render_the_layout(self):
        self.tc.render({ 'baconus': 'bacon' })
        self.tc.layout.render.assert_called_once_with(
            self.tc.terminal, { 'baconus': 'bacon' })

    def test_it_should_return_a_default_state_with_no_tweets(self):
        state = self.tc._initialState()
        assert state['lists'] == {}

    @patch('shutil.get_terminal_size', lambda: [80, 20])
    def test_it_should_append_terminal_dims_to_state(self):
        state = {}
        state = self.tc._appendDims(state)
        assert state == { 'screen_width': 80, 'screen_height': 20 }

    def test_it_should_get_a_key_input(self):
        self.tc._handleKey(self.tc.terminal)
        self.tc.terminal.inkey.assert_called_once_with(timeout = 0.1)

    def test_it_should_convert_complex_key_inputs(self):
        keypress = Mock()
        keypress.is_sequence = True
        keypress.name = 'Mock Keypress'

        self.tc.terminal.inkey = Mock(return_value=keypress)
        result = self.tc._handleKey(self.tc.terminal)

        assert result == 'Mock Keypress'

    def test_it_should_fire_up_the_event_loop(self):
        self.tc._startEventLoop = Mock()
        self.tc.run()
        assert self.tc.terminal.enter_fullscreen.call_count == 1
        assert self.tc.terminal.exit_fullscreen.call_count == 1

    def test_it_should_fail_gracefully_from_on_close(self):
        e = KeyboardInterrupt()
        mockLoop = Mock()
        mockLoop.side_effect = e
        self.tc._startEventLoop = mockLoop

        self.tc.run()
        assert self.tc.terminal.enter_fullscreen.call_count == 1
        assert self.tc.terminal.exit_fullscreen.call_count == 1
