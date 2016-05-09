import sys
import readchar
import shutil
import html
import os

from TwitterCLI.Tweet import Tweet
from TwitterCLI.Screen import Screen
from TwitterCLI.fetch_tweets import fetch_tweets

from blessed import Terminal

def main():
    timeline = fetch_tweets()
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

if __name__ == "__main__":
    main()
