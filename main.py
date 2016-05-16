from TwitterCLI.app import TwitterClient
from TweetSource.app import main as ts_func

from time import sleep
from threading import Thread
from queue import Queue

import json
from TweetSource import TweetFetcher
from TweetSource.utils import getTwitter
from TweetSource import TwitterWrapper

import pymongo

def main():
    mongo = pymongo.MongoClient('localhost', 27010)
    db = mongo['twitter-cli']

    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)
    twitter = getTwitter(config)
    tweetSource = TwitterWrapper(config, twitter)
    tweetFetcher = TweetFetcher(tweetSource, db)

    q = Queue()
    t = Thread(target=ts_func, args=(q, tweetFetcher))
    t.daemon = True
    t.start()

    app = TwitterClient(q)
    app.run()
    return

if __name__ == "__main__":
    main()
