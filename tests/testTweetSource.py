import unittest
from mock import MagicMock as Mock

from TweetSource.TweetSource import TweetSource

class TestTweetSource(unittest.TestCase):
    def setUp(self):
        self.twitter = Mock()
        self.mongodb = Mock()
        self.config = { 'user' : 'grob' }
        self.ts = TweetSource(self.config, self.twitter, self.mongodb)

    def test_it_should_fetch_latest_tweets_from_twitter(self):
        self.ts._getNewTweets(since=800)
        self.twitter.statuses.user_timeline.assert_called_once_with(
            screen_name='grob',
            include_rts=False,
            since=800
        )
    def test_it_should_fetch_some_tweets_from_twitter(self):
        self.ts._getNewTweets()
        self.twitter.statuses.user_timeline.assert_called_once_with(
            screen_name='grob',
            include_rts=False
        )
