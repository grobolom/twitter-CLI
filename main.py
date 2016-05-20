import asyncio
import traceback
import os

from TwitterCLI.app import TwitterClient
from TwitterCLI.reducers import RootReducer
from TweetSource.app import TweetSource as TweetSource
from TweetSource.app import main as ts_func
from TweetSource.app import getAllTweets
from TwitterCLI.middleware import TweetSourceMiddleware

from time import sleep
from threading import Thread
from queue import Queue

import json
from TweetSource import TweetFetcher
from TweetSource import MongoTweetSource
from TweetSource.utils import getTwitter
from TweetSource import TwitterWrapper

import pymongo

def main():
    mongo = pymongo.MongoClient('localhost', 27017)
    try:
        db = mongo['twitter-cli']

        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)
        twitter = getTwitter(config)
        tweetSource = TwitterWrapper(config, twitter)
        mongoSource = MongoTweetSource(db)
        tweetFetcher = TweetFetcher(tweetSource, mongoSource)

        TweetSourceInbox = asyncio.Queue()
        TwitterCLIInbox = asyncio.Queue()
        middlewares = []
        middlewares = [ TweetSourceMiddleware(TweetSourceInbox) ]
        reducer = RootReducer(middlewares=middlewares)

        ts = TweetSource(TweetSourceInbox, TwitterCLIInbox, tweetFetcher)

        loop = asyncio.get_event_loop()
        asyncio.async(ts.run())
        app = TwitterClient(TwitterCLIInbox, reducer=reducer)
        loop.run_until_complete(app.run())

    except (KeyboardInterrupt, Exception) as e:
        os.system('clear')
        traceback.print_exc()
    finally:
        mongo.close()
    return
if __name__ == "__main__":
    main()
