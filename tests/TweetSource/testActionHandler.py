import unittest
from mock import MagicMock as Mock
from TweetSource import ActionHandler

class TestActionHandler(unittest.TestCase):
    def setUp(self):
        self.tf = Mock()
        self.ah = ActionHandler(self.tf)

    def test_it_should_get_new_tweets(self):
        action = {
            'name': 'GET_TWEETS',
            'since': 12301203,
        }
        self.ah.handleAction(action)
        self.tf.getTweets.assert_called_once_with(since=12301203)
