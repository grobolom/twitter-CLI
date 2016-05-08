import json
from TwitterCLI.Tweet import Tweet

class TweetBuilder:
    def buildTweet(self, tweet_json):
        try:
            tweet = json.loads(tweet_json)
        except:
            pass
        return Tweet(tweet['user']['screen_name'], tweet['text'])
