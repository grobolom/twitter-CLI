import unittest

from TwitterCLI.reducers import RootReducer

class TestRootReducer(unittest.TestCase):
    def setUp(self):
        self.rootReducer = RootReducer()

    def test_it_should_return_the_same_state_if_action_is_invalid(self):
        state = {
            'cursor': 50,
        }
        action = {
            'name' : 'INVALID_ACTION123'
        }
        new_state = self.rootReducer.reduce(state, action)
        self.assertEquals(new_state, state)

    def test_scrolls_cursor_down(self):
        state = {
            'selected_list': 'friends',
            'lists': {
                'friends': {
                    'cursor' : 0,
                    'cursor_max' : 20,
                }
            }
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : 1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['lists']['friends']['cursor'], 1)

    def test_stops_cursor_scrolling_past_end_of_page(self):
        state = {
            'selected_list': 'friends',
            'lists': {
                'friends': {
                    'cursor' : 20,
                    'cursor_max' : 20,
                }
            }
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : 1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['lists']['friends']['cursor'], 20)

    def test_scrolls_cursor_up(self):
        state = {
            'selected_list': 'friends',
            'lists': {
                'friends': {
                    'cursor' : 10,
                    'cursor_max' : 20,
                }
            }
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : -1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['lists']['friends']['cursor'], 9)

    def test_stops_cursor_scrolling_above_top_of_page(self):
        state = {
            'selected_list': 'friends',
            'lists': {
                'friends': {
                    'cursor' : 0,
                    'cursor_max' : 20,
                }
            }
        }
        action = {
            'name' : 'CURSOR_MOVE',
            'amount' : -1,
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['lists']['friends']['cursor'], 0)

    def test_it_should_switch_lists_on_tab(self):
        state = {
            'selected_list': 'tweets',
            'lists': {
                'tweets': [],
                'list.next': [],
            }
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'list.next')

    def test_it_should_switch_to_first_list_after_last(self):
        state = {
            'selected_list': 'list.next',
            'lists': {
                'tweets': [],
                'list.next': [],
            }
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'tweets')

    def test_it_should_select_the_first_tab_if_invalid_tab_selected(self):
        state = {
            'selected_list': 'notreal',
            'lists': {
                'tweets': [],
            }
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state['selected_list'], 'tweets')

    def test_it_should_switch_tabs_in_the_correct_order(self):
        state = {
            'selected_list': 'tweets',
            'lists': {
                'tweets': [],
                'list.friends': [],
                'list.enemies': [],
            }
        }
        action = {
            'name' : 'SWITCH_TAB',
        }
        state_one = self.rootReducer.reduce(state, action)
        self.assertEqual(state_one['selected_list'], 'list.enemies')

    def test_it_should_switch_views(self):
        state = { 'view': 'splash' }
        action = { 'name': 'SWITCH_VIEW', 'target' : 'anotherview' }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state, { 'view': 'anotherview' })

    def test_it_should_add_a_list_of_tweets(self):
        state = { 'lists': {} }
        action = {
            'name': 'NEW_TWEETS',
            'tweets': [ {} ],
            'list': 'friends',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state, {
            'lists': {
                'friends': {
                    'tweets': [ {} ],
                    'cursor': 0,
                    'cursor_max': 1,
                }
            }
        })

    def test_it_should_append_new_tweets(self):
        state = {
            'lists': {
                'friends': {
                    'tweets': [ { 'text' : 'first_tweet' } ],
                }
            }
        }
        action = {
            'name': 'NEW_TWEETS',
            'tweets': [ { 'text': 'second_tweet' } ],
            'list': 'friends',
        }
        state = self.rootReducer.reduce(state, action)
        self.assertEqual(state, {
            'lists': {
                'friends': {
                    'tweets': [
                        { 'text' : 'first_tweet' },
                        { 'text' : 'second_tweet' },
                    ]
                }
            }
        })

    def test_it_should_not_shallow_copy_state(self):
        state = {
            'lists': {
                'friends': {
                    'tweets': [ { 'text' : 'first_tweet' } ],
                }
            }
        }
        action = {
            'name': 'NEW_TWEETS',
            'tweets': [ { 'text': 'second_tweet' } ],
            'list': 'friends',
        }
        new_state = self.rootReducer.reduce(state, action)
        self.assertNotEqual(state, new_state)
