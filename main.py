import sys
import readchar
import json
import shutil
import html
import os

from twitter import Twitter, OAuth
from TwitterCLI.Tweet import Tweet
from TwitterCLI.Screen import Screen

from blessed import Terminal

def main():
    timeline = fetch()
    dims = shutil.get_terminal_size()
    screen = Screen(dims[1], dims[0])

    tweets = []
    for tweet in timeline:
        author = tweet['user']['screen_name']
        text = html.unescape(tweet['text'].replace('\u2026','').rstrip(' \n'))
        tweets.append(Tweet(author, text))

    term = Terminal()
    key = 0
    do = ''

    with term.fullscreen():
        while key != '\x03':
            if key == 'd':
                tweets = tweets[1::]
                do = 'clear'
            render(term, screen, tweets, do)
            key = readchar.readkey()

def render(term, screen, tweets, do):
    if do == 'clear':
        print(term.clear)
    with term.location(0, 0):
        screen.render(tweets)


def fetch():
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

        timeline = twitter.statuses.user_timeline(screen_name=user)

        with open('config/data.json', 'w') as temp_data:
            json.dump(timeline, temp_data)

    return timeline

if __name__ == "__main__":
    main()
