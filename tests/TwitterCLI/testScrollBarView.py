import unittest
from TwitterCLI.views import ScrollBar

class TestScrollBarView(unittest.TestCase):
    def test_it_should_display_a_scrollbar(self):
        height      = 20
        cursor      = 17
        cursor_max  = 100
        page_height = 10

        scrollbar = ScrollBar()
        result = scrollbar.render(
            height,
            cursor,
            cursor_max,
            page_height
        )
        self.assertEqual("".join(result),
            "   " + chr(9608) * 2 + "               ")

        height      = 10
        cursor      = 35
        cursor_max  = 100
        page_height = 10

        scrollbar = ScrollBar()
        result = scrollbar.render(
            height,
            cursor,
            cursor_max,
            page_height
        )
        self.assertEqual("".join(result),
            "   " + chr(9608) + "      ")
