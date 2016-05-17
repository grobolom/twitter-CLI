import unittest

from TwitterCLI.actions import KeyboardEventHandler

class TestKeyboardEventHandler(unittest.TestCase):
    def test_it_should_map_cursor_events(self):
        handler = KeyboardEventHandler()
        key = 'j'
        actual = handler.getAction(key, {})
        assert actual == { 'name': 'CURSOR_MOVE', 'amount': 1 }

    def test_it_should_return_an_empty_event_when_no_key_mapping_found(self):
        handler = KeyboardEventHandler()
        key = '`'
        actual = handler.getAction(key, {})
        assert actual == { 'name': 'None' }

    def test_it_should_ask_for_new_tweets(self):
        handler = KeyboardEventHandler()
        key = 'KEY_ENTER'
        state = {
            'selected_list': 'tweets',
            'lists': {
                'tweets': [
                    { 'id': 800 },
                    { 'id': 500 },
                ],
            }
        }
        actual = handler.getAction(key, state)
        expected = {
            'name': 'GET_TWEETS',
            'since': 800,
        }
        assert actual == expected
