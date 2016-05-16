import unittest

from TwitterCLI.TweetBuilder import TweetBuilder
from TwitterCLI.Tweet import Tweet

class TestTweetBuilder(unittest.TestCase):
    def test_creates_tweet_from_json(self):
        json = '''
        {
            "user": {
                "screen_name":"grobolom"
            },
            "text":"something"
        }
        '''
        expected = Tweet('grobolom', 'something')

        builder = TweetBuilder()
        actual = builder.buildTweet(json)

        self.assertEqual(expected.author, actual.author)
        self.assertEqual(expected.text, actual.text)

    def test_throws_exception_on_invalid_json(self):
        builder = TweetBuilder()
        with self.assertRaisesRegexp(TypeError, 'invalid json'):
            builder.buildTweet('bogus')

    def test_builds_multiple_tweets_from_list(self):
        tweet_list = [
            {
                'user': { 'screen_name': 'cow' },
                'text': 'moo',
            }, {
                'user': { 'screen_name': 'human' },
                'text': 'wha\xfft?',
            },
        ]
        builder = TweetBuilder()
        actual = builder.buildTweets(tweet_list)

        self.assertEqual('cow', actual[0].author)
        self.assertEqual('wha.t?', actual[1].text)
