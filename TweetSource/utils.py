from twitter import Twitter, OAuth

def getTwitter(config):
    access_key = config['access_key']
    access_secret = config['access_secret']
    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']

    return Twitter(
        auth = OAuth(
            access_key,
            access_secret,
            consumer_key,
            consumer_secret
        )
    )
