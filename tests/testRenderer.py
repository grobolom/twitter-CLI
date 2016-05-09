import unittest

from TwitterCLI.Renderer import Renderer
from TwitterCLI.Tweet import Tweet

class TestRenderer(unittest.TestCase):
    def test_it_should_render_tweets(self):
        renderer = Renderer()
        tweet = Tweet('grobolom', 'bacon\n bacon')
        self.assertEqual(renderer.render(tweet), [
            "\033[92m       grobolom \033[0mbacon",
            "                 bacon",
        ])
