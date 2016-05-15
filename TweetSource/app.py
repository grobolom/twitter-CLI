from TweetSource.TweetSource import TweetSource
from TweetSource.modules import TweetFetcher
from TweetSource.utils import getTwitter

import json
from time import sleep

def main(client_queue):
    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)
    twitter = getTwitter(config)
    tweetSource = TweetSource(config, twitter)
    tweetFetcher = TweetFetcher(tweetSource)

    client_queue.put({
        'name': 'NEW_TWEETS',
        'list': 'tweets',
        'tweets': tweetFetcher.getTweets()
    })
    client_queue.put({
        'name': 'NEW_TWEETS',
        'list': 'home_timeline',
        'tweets': tweetFetcher.getHomeTimeline()
    })
    lists = tweetFetcher.getLists()
    for _list in lists:
        client_queue.put({
            'name': 'NEW_TWEETS',
            'list': 'list.' + _list,
            'tweets': tweetFetcher.getListTweets(_list)
        })
