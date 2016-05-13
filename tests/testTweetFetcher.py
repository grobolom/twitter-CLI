import unittest
from mock import MagicMock as Mock

from TweetSource.modules import TweetFetcher

class TestTweetFetcher(unittest.TestCase):
    def setUp(self):
        self.source = Mock()
        self.source.getNewTweets = Mock(return_value="""
        [{
            "user": {
                "screen_name":"grobolom"
            },
            "text":"something"
        }]
        """)
        self.tf = TweetFetcher(self.source)

    def test_it_should_return_tweets(self):
        result = self.tf.getTweets()
        self.assertEqual([ result[0].author, result[0].text ],
            [ 'grobolom', 'something' ])
