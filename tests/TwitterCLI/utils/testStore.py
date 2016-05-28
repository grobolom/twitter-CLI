import unittest

from TwitterCLI.utils import Store

class TestStore(unittest.TestCase):
    def test_it_should_get_an_initial_state(self):
        initialState = { 'something': 'else' }
        reducers = []
        s = Store(reducers, initialState)
        assert s.getState() == initialState
