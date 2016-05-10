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
