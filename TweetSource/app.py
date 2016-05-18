from . import ActionHandler

def main(client_queue, tweetFetcher):
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

class TweetSource:
    def __init__(self, in_q, out_q, tf):
        self.in_q = in_q
        self.out_q = out_q
        self.tf = tf
        self.ah = ActionHandler(tf)

    def run(self):
        getAllTweets(self.out_q, self.tf)
        while True:
            action = None
            try:
                action = self.in_q.get()
            except:
                pass

            if action:
                res = self.ah.handleAction(action)
                if res:
                    self.out_q.put(res)
