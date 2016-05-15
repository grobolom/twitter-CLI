from TweetSource.TweetSource import TweetSource
from TweetSource.modules import TweetFetcher
from TweetSource.utils import getTwitter

def main(client_queue):
    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)
    twitter = getTwitter(config)
    tweetSource = TweetSource(config, twitter)
    tweetFetcher = TweetFetcher(tweetSource)

    sleep(2)
    client_queue.put({
        'name': 'NEW_TWEETS',
        'list': 'home_timeline',
        'tweets': tweetFetcher.getHomeTimeline()
    })
    sleep(2)
    client_queue.put({
        'name': 'NEW_TWEETS',
        'list': 'tweets',
        'tweets': tweetFetcher.getTweets()
    })
    sleep(2)
    lists = tweetFetcher.getLists()
    for _list in lists:
        sleep(2)
        client_queue.put({
            'name': 'NEW_TWEETS',
            'list': 'list.' + _list,
            'tweets': tweetFetcher.getListTweets(_list)
        })
