import json
from twitter import Twitter, OAuth

def fetch_tweets():
    timeline = None
    try:
        with open('config/data.json') as cached_data:
            timeline = json.load(cached_data)
    except IOError:
        pass

    if not timeline:
        print('fetching')
        with open('config/twitter.json') as twitter_config:
            config = json.load(twitter_config)

        user = config['user']
        access_key = config['access_key']
        access_secret = config['access_secret']
        consumer_key = config['consumer_key']
        consumer_secret = config['consumer_secret']

        twitter = Twitter(
            auth = OAuth(
                access_key,
                access_secret,
                consumer_key,
                consumer_secret
            )
        )

        timeline = twitter.lists.statuses(
            slug='friends',
            owner_screen_name=user,
            include_rts=False,
            count=200
        )

        with open('config/data.json', 'w') as temp_data:
            json.dump(timeline, temp_data)

    return timeline
