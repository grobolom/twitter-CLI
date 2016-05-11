import unittest

from TwitterCLI.actions import KeyboardEventHandler

class TestKeyboardEventHandler(unittest.TestCase):
    def test_it_should_map_cursor_events(self):
        handler = KeyboardEventHandler()
        key = 'j'
        actual = handler.getAction(key)
        self.assertEqual(actual, { 'name': 'CURSOR_MOVE', 'amount': 1 })
