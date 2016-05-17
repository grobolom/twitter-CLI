import unittest
from mock import MagicMock as Mock
from TweetSource import MongoTweetSource

class TestMongoTweetSource(unittest.TestCase):
    def setUp(self):
        self.db = Mock()
        self.mts = MongoTweetSource(self.db)

    def test_it_should_fetch_some_tweets_from_mongo(self):
        self.mts.getNewTweets()
        assert self.db.tweets.find.call_count == 1

    def test_it_should_save_tweets_to_mongo(self):
        self.mts.saveTweets([{ 'user': 'grob' }])
        assert self.db.tweets.insert.call_count == 1

    def test_it_should_fetch_the_home_timeline_from_mongo(self):
        self.mts.getHomeTimeline()
        assert self.db.home_timeline.find.call_count == 1

    def test_it_should_save_home_timeline(self):
        self.mts.saveHomeTimeline([{ 'user': 'grob' }])
        assert self.db.home_timeline.insert.call_count == 1

    def test_it_should_fetch_the_list_names(self):
        self.mts.getLists()
        assert self.db.list_names.find.call_count == 1

    def test_it_should_save_the_list_names(self):
        self.mts.saveLists([{ 'name': 'friends' }])
        assert self.db.list_names.insert.call_count == 1

    def test_it_should_fetch_list_tweets(self):
        self.mts.getListTweets()
        assert self.db.lists.find.call_count == 1

    def test_it_should_save_list_tweets(self):
        self.mts.saveListTweets([{ 'user': 'grob' }])
        assert self.db.lists.insert.call_count == 1
