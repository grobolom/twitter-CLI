import unittest
from mock import MagicMock as Mock
from mock import call
from TwitterCLI.Screen import Screen

import sys
from io import StringIO

class TestScreen(unittest.TestCase):
    """
    this test is a bit difficult to do because the Screen() class is at
    the boundary of our classes. It has to work directly with ncurses/
    the terminal and this means it has to make calls to print, which
    means we have some funky stuff. Hopefully this rudimentary test
    is enough anyway.
    """
    def setUp(self):
        self.output       = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout        = self.output

    def tearDown(self):
        self.output.close()
        self.stdout = self.saved_stdout

    def test_it_should_render_a_basic_layout(self):
        screen = Screen()
        term = Mock()
        layout = [
            (2 , 1, ['wut', 'butt'])
        ]

        actual = screen.render(term, layout)
        self.assertEqual(self.output.getvalue(), "wut\nbutt\n")
        term.move.assert_has_calls(
            [
                call(0, 0),
                call(0, 0),
            ],
            any_order = False
        )
        term.location.assert_has_calls(
            [
                call(2, 1),
                call(2, 2),
            ],
            any_order = True
        )
