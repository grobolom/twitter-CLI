import unittest
from TwitterCLI.views import SplashScreen

class TestSplashScreenView(unittest.TestCase):
    def test_it_should_display_text_correctly(self):
        text = [
            "loading tweets...",
            "and something",
        ]
        width = 20
        height = 5
        s = SplashScreen()
        result = s.render(text, width, height)
        self.assertEqual(result, [
            "                    ",
            "  loading tweets... ",
            "    and something   ",
            "                    ",
            "                    ",
        ])
