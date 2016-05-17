from TwitterCLI.app import TwitterClient
from TwitterCLI.reducers import RootReducer
from TweetSource.app import main as ts_func
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

        outq = Queue()
        middlewares = [ TweetSourceMiddleware(outq) ]
        reducer = RootReducer(middlewares=middlewares)

        q = Queue()
        t = Thread(target=ts_func, args=(q, tweetFetcher))
        t.daemon = True
        t.start()

        app = TwitterClient(q, reducer=reducer)
        app.run()
    except:
        pass
    finally:
        mongo.close()
    return
if __name__ == "__main__":
    main()
