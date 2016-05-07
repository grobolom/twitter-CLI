import unittest

from TwitterCLI.Renderer import Renderer

class TestRenderer(unittest.TestCase):
    def test(self):
        x = Renderer()
        x.render('bacon\n\n\nbacon')
