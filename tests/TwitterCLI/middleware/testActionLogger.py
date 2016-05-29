import unittest

from TwitterCLI.middleware import ActionLogger

class TestActionLogger(unittest.TestCase):
    def test_it_should_bottom_out_at_depth_1(self):
        d = {
            'a': [1],
            'b': (1, 2),
            'c': {'x':'y'},
            'd': 1,
            'e': '2',
        }
        sut = ActionLogger('')
        res = sut._getThinObject(d)

        assert type(res['a']) == str
        assert type(res['b']) == str
        assert type(res['c']) == str
        assert type(res['d']) == int
        assert type(res['e']) == str
