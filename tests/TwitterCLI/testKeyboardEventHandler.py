import unittest

from TwitterCLI.actions import KeyboardEventHandler

class TestKeyboardEventHandler(unittest.TestCase):
    def test_it_should_map_cursor_events(self):
        handler = KeyboardEventHandler()
        key = 'j'
        actual = handler.getAction(key)
        self.assertEqual(actual, { 'name': 'CURSOR_MOVE', 'amount': 1 })

    def test_it_should_return_an_empty_event_when_no_key_mapping_found(self):
        handler = KeyboardEventHandler()
        key = '`'
        actual = handler.getAction(key)
        self.assertEqual(actual, { 'name': 'None' })
