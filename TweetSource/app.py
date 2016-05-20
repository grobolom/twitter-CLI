from . import ActionHandler
from queue import Empty
import traceback
import time
import asyncio

def main(client_queue, tweetFetcher):
    getAllTweets(client_queue, tweetFetcher)

@asyncio.coroutine
def getAllTweets(queue, tweetFetcher):
    try:
        yield from queue.put({
            'name': 'NEW_TWEETS',
            'list': 'tweets',
            'tweets': tweetFetcher.getTweets()
        })
        yield from queue.put({
            'name': 'NEW_TWEETS',
            'list': 'home_timeline',
            'tweets': tweetFetcher.getHomeTimeline()
        })
        lists = tweetFetcher.getLists()
        for _list in lists:
            yield from queue.put({
                'name': 'NEW_TWEETS',
                'list': 'list.' + _list,
                'tweets': tweetFetcher.getListTweets(_list)
            })
    except:
        pass
    return

class TweetSource:
    def __init__(self, in_q, out_q, tf):
        self.in_q = in_q
        self.out_q = out_q
        self.tf = tf
        self.ah = ActionHandler(tf)

    @asyncio.coroutine
    def run(self):
        yield from getAllTweets(self.out_q, self.tf)
        try:
            while True:
                action = None
                try:
                    action = yield from self.in_q.get()
                except Empty as e:
                    pass

                if action:
                    res = self.ah.handleAction(action)
                    if res:
                        yield from self.out_q.put(res)
        except:
            traceback.print_exc()
