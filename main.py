import sys
import readchar
import shutil
import html
import os
import re

from TwitterCLI.Tweet import Tweet
from TwitterCLI.Screen import Screen
from TwitterCLI.views.TimelineView import TimelineView
from TwitterCLI.fetch_tweets import fetch_tweets

from blessed import Terminal

def main():
    timeline = fetch_tweets()
    dims = shutil.get_terminal_size()
    tl = TimelineView(80, dims[1] - 1)

    tweets = []
    for tweet in timeline:
        author = tweet['user']['screen_name']
        text = re.sub(r'[^\x00-\x7f]', r'.', html.unescape(tweet['text']))
        text = text.replace('\n', ' ')
        tweets.append(Tweet(author, text))

    term = Terminal()
    key = 0
    do = ''
    cursor = 0
    s = Screen()

    with term.fullscreen():
        while key != '\x03':
            if key == 'k':
                cursor -= 1
            if key == 'j':
                cursor += 1
            s.render(term, [
                (0, 0, tl.render(tweets, cursor)),
                (158, 0, [str(len(tweets)), str(cursor)]),
            ])
            key = readchar.readkey()

if __name__ == "__main__":
    main()
