import unittest

from TwitterCLI.TwitterHandler import TwitterHandler

class CacheStub:
    def getTweets(self):
        return [{'id': '1', 'user': 'grobolom', 'text': 'whee'}]

class TestTwitterHandler(unittest.TestCase):
    def test_it_should_fetch_tweets_from_cache(self):
        cache = CacheStub()
        handler = TwitterHandler({}, cache);
        tweets = handler.getTweets()
        self.assertEqual(
            [{'id': '1', 'user': 'grobolom', 'text': 'whee'}],
            tweets)

    def test_it_should_return_real_tweets_without_cache(self):
        handler = TwitterHandler({});
        tweets = handler.getTweets()
        self.assertEqual([], tweets)
