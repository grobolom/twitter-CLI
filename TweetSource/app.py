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
    """
    lists = tweetFetcher.getLists()
    for _list in lists:
        queue.put({
            'name': 'NEW_TWEETS',
            'list': 'list.' + _list,
            'tweets': tweetFetcher.getListTweets(_list)
        })
    ""
