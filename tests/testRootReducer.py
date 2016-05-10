import unittest

from TwitterCLI.reducers import RootReducer

class TestRootReducer(unittest.TestCase):
    def setUp(self):
        self.rootReducer = RootReducer()

    def test_scrolls_cursor_down(self):
        state = {
            'cursor' : 0,
            'cursor_max' : 20,
        }
        state = self.rootReducer.reduce(state, 'CURSOR_DOWN')
        self.assertEqual(state['cursor'], 1)
        pass
    def test_stops_cursor_scrolling_past_end_of_page(self):
        state = {
            'cursor' : 20,
            'cursor_max' : 20,
        }
        state = self.rootReducer.reduce(state, 'CURSOR_DOWN')
        self.assertEqual(state['cursor'], 20)
        pass
    def test_scrolls_cursor_up(self):
        state = {
            'cursor' : 10,
            'cursor_max' : 20,
        }
        state = self.rootReducer.reduce(state, 'CURSOR_UP')
        self.assertEqual(state['cursor'], 9)
        pass
    def test_stops_cursor_scrolling_above_top_of_page(self):
        state = {
            'cursor' : 0,
            'cursor_max' : 20,
        }
        state = self.rootReducer.reduce(state, 'CURSOR_UP')
        self.assertEqual(state['cursor'], 0)
        pass