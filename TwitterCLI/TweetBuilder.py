import json
import re
import html

from TwitterCLI.Tweet import Tweet

class TweetBuilder:
    def buildTweet(self, tweet_json):
        try:
            tweet = json.loads(tweet_json)
        except(ValueError):
            raise TypeError('invalid json')
        return Tweet(tweet['user']['screen_name'], tweet['text'])

    def buildTweets(self, tweet_list):
        """
        build a bunch of properly formatted tweets from a 'json.dump'ed
        list

        we don't allow tweets to have special chars so we strip them
        out here. Maybe not the right place but bleh
        """
        result = []
        for tweet in tweet_list:
            result += [ self._buildTweetFromObject(tweet) ]
        return result

    def _buildTweetFromObject(self, tweet):
        author = tweet['user']['screen_name']
        text = re.sub(r'[^\x00-\x7f]', r'.', html.unescape(tweet['text']))
        text = text.replace('\n', ' ')
        return Tweet(author, text)

