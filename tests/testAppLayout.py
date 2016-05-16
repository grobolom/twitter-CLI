from TwitterCLI.layout import AppLayout
import unittest
from mock import MagicMock as Mock

class TestAppLayout(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.term = Mock()
        self.al = AppLayout(screen=self.screen)

        self.al.splashView = Mock()
        self.al.mainView = Mock()

    def test_it_should_default_to_the_main_view(self):
        state = {
            'screen_width': 40,
            'screen_height': 20,
            'view': 'random',
        }
        self.al.render(self.term, state)

        self.al.mainView.assert_called_once()
        self.al.splashView.assert_not_called()

    def test_it_should_show_the_splash_screen(self):
        state = {
            'screen_width': 40,
            'screen_height': 20,
            'view': 'splash',
        }
        self.al.render(self.term, state)

        self.al.mainView.assert_not_called()
        self.al.splashView.assert_called_once()

