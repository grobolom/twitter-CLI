import unittest
from mock import MagicMock as Mock

from TweetSource.modules import TweetFetcher

class TestTweetFetcher(unittest.TestCase):
    def setUp(self):
        fakeTweets = [
            {
                "user": {
                    "screen_name": "grobolom"
                },
                "text": "something"
            }
        ]

        self.source = Mock()
        self.source.getNewTweets    = Mock(return_value=fakeTweets)
        self.source.getListTweets   = Mock(return_value=fakeTweets)
        self.source.getHomeTimeline = Mock(return_value=fakeTweets)
        self.source.getLists        = Mock(return_value=[
            { "name": "friends" },
            { "name": "enemies" }
        ])
        self.tf = TweetFetcher(self.source)

    def test_it_should_return_tweets(self):
        result = self.tf.getTweets()
        self.assertEqual([ result[0].author, result[0].text ],
            [ 'grobolom', 'something' ])

    def test_it_should_return_lists(self):
        result = self.tf.getLists()
        self.assertEqual(result, [ 'friends', 'enemies' ])

    def test_it_should_return_list_tweets(self):
        result = self.tf.getListTweets('friends')
        self.assertEqual([ result[0].author, result[0].text ],
            [ 'grobolom', 'something' ])

    def test_it_should_return_a_home_timeline(self):
        result = self.tf.getHomeTimeline()
        self.assertEqual([ result[0].author, result[0].text ],
            [ 'grobolom', 'something' ])
