import json
from twitter import Twitter, OAuth
from TwitterCLI.TweetBuilder import TweetBuilder

def fetch_tweets():
    timeline = None
    try:
        with open('config/tweets.json') as cached_data:
            timeline = json.load(cached_data)
    except IOError:
        pass

    if not timeline:
        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)

        user = config['user']
        twitter = _getTwitter(config)
        timeline = twitter.statuses.user_timeline(
            screen_name=user,
            include_rts=False,
            count=200
        )

        with open('config/tweets.json', 'w') as temp_data:
            json.dump(timeline, temp_data)

    tb = TweetBuilder()
    return tb.buildTweets(timeline)

def fetch_friend_list():
    timeline = None
    try:
        with open('config/lists.friends.json') as cached_data:
            timeline = json.load(cached_data)
    except IOError:
        pass

    if not timeline:
        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)

        user = config['user']
        twitter = _getTwitter(config)
        timeline = twitter.lists.statuses(
            slug='friends',
            owner_screen_name=user,
            include_rts=False,
            count=200
        )

        with open('config/lists.friends.json', 'w') as temp_data:
            json.dump(timeline, temp_data)

    tb = TweetBuilder()
    return tb.buildTweets(timeline)

def _getTwitter(config):
    access_key = config['access_key']
    access_secret = config['access_secret']
    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']

    return Twitter(
        auth = OAuth(
            access_key,
            access_secret,
            consumer_key,
            consumer_secret
        )
    )
