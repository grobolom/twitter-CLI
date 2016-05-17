import unittest
from mock import MagicMock as Mock

from TweetSource import TweetFetcher

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

        self.source  = Mock()
        self.source.getNewTweets    = Mock(return_value=fakeTweets)
        self.source.getListTweets   = Mock(return_value=fakeTweets)
        self.source.getHomeTimeline = Mock(return_value=fakeTweets)
        self.source.getLists        = Mock(return_value=[
            { "name": "friends" },
            { "name": "enemies" }
        ])

        self.msource = Mock()

        self.tf = TweetFetcher(self.source, self.msource)

    def test_it_should_get_mongo_tweets_first(self):
        mongo_tweets = [{
            'user': {
                'screen_name': 'wut'
            },
            'text': 'nothing'
        }]
        self.msource.getNewTweets = Mock(return_value=mongo_tweets)
        result = self.tf.getTweets()
        assert [result[0].author, result[0].text] == ['wut', 'nothing']

    def test_it_should_return_tweets(self):
        self.msource.getNewTweets = Mock(return_value=None)
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
