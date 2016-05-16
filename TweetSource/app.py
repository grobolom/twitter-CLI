from TweetSource import TwitterWrapper
from TweetSource import TweetFetcher
from TweetSource.utils import getTwitter

import json

def main(client_queue):
    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)
    twitter = getTwitter(config)
    tweetSource = TwitterWrapper(config, twitter)
    tweetFetcher = TweetFetcher(tweetSource)

    getAllTweets(client_queue, tweetFetcher)

def getAllTweets(queue, tweetFetcher):
    queue.put({
        'name': 'NEW_TWEETS',
        'list': 'tweets',
        'tweets': tweetFetcher.getTweets()
    })
    queue.put({
        'name': 'NEW_TWEETS',
        'list': 'home_timeline',
        'tweets': tweetFetcher.getHomeTimeline()
    })
    lists = tweetFetcher.getLists()
    for _list in lists:
        queue.put({
            'name': 'NEW_TWEETS',
            'list': 'list.' + _list,
            'tweets': tweetFetcher.getListTweets(_list)
        })
