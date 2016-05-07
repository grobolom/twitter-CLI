import sys
import readchar
import json

from twitter import Twitter, OAuth

def main():
    print('fetch data from the api')

    fetch()

    print('loop')
    print('   shove data + action into reducer to get a visual representation')
    print('   push it into a renderer to get an 80x40 printout of it')
    print('   wait for commands from the user')

    key = 0
    while key != 27:
        key = ord(readchar.readchar())
        print(key)

def fetch():
    with open('config/twitter.json') as twitter_config:
        config = json.load(twitter_config)

    user = config['user']
    access_key = config['access_key']
    access_secret = config['access_secret']
    consumer_key = config['consumer_key']
    consumer_secret = config['consumer_secret']

    twitter = Twitter(
        auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

    print(twitter.statuses.user_timeline(screen_name=user))

if __name__ == "__main__":
    main()
