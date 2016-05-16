import unittest
import twitter
from TweetSource.utils import getTwitter

class TestUtils(unittest.TestCase):
    def test_it_should_return_a_twitter_object(self):
        config = {
            'access_key': '',
            'access_secret': '',
            'consumer_key': '',
            'consumer_secret': '',
        }
        actual = getTwitter(config)
        self.assertIsInstance(actual, twitter.Twitter)
