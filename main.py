from TwitterCLI.app import TwitterClient
from TweetSource.app import main as ts_func

from time import sleep
from threading import Thread
from queue import Queue


def main():
    q = Queue()
    t = Thread(target=ts_func, args=(q,))
    t.daemon = True
    t.start()

    app = TwitterClient(q)
    app.run()
    return

if __name__ == "__main__":
    main()
