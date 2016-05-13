import unittest

from TwitterCLI.containers import VerticalScrollBar
from TwitterCLI.views import ScrollBar

class TestVerticalScrollBar(unittest.TestCase):
    def test_it_should_the_scrollbar(self):
        view = ScrollBar()
        container = VerticalScrollBar()

        state = {
            'screen_height': 20,
            'cursor': 50,
            'cursor_max': 520,
        }
        actual = container.render(state)
        expected = view.render(19, 50, 520, 19)
        self.assertEqual(actual, expected)
