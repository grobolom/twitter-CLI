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
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : 1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['cursor'], 1)

    def test_stops_cursor_scrolling_past_end_of_page(self):
        state = {
            'cursor' : 20,
            'cursor_max' : 20,
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : 1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['cursor'], 20)

    def test_scrolls_cursor_up(self):
        state = {
            'cursor' : 10,
            'cursor_max' : 20,
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : -1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['cursor'], 9)

    def test_stops_cursor_scrolling_above_top_of_page(self):
        state = {
            'cursor' : 0,
            'cursor_max' : 20,
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : -1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['cursor'], 0)

    def test_it_should_switch_lists_on_tab(self):
        state = {
            'selected_list': 'tweets',
            'available_lists': [
                'tweets',
                'list.next',
            ]
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'list.next')

    def test_it_should_switch_to_first_list_after_last(self):
        state = {
            'selected_list': 'list.next',
            'available_lists': [
                'tweets',
                'list.next',
            ]
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'tweets')

    def test_it_should_select_the_first_tab_if_invalid_tab_selected(self):
        state = {
            'selected_list': 'notreal',
            'available_lists': [
                'tweets',
            ]
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'tweets')

