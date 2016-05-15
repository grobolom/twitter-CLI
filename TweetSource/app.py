def main():
    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)
    twitter = getTwitter(config)
    tweetSource = TweetSource(config, twitter)
    tweetFetcher = TweetFetcher(tweetSource)

    sleep(1)
