import shutil
from queue import Queue
from TwitterCLI.app import TwitterClient

from time import sleep
from threading import Thread

def move_tab_later(q):
    while True:
        sleep(2)
        action = { 'name': 'SWITCH_TAB' }
        q.put(action)

def main():
    q = Queue()
    t = Thread(target=move_tab_later, args=(q,))
    t.daemon = True
    t.start()

    app = TwitterClient(q)
    app.run()
    return

if __name__ == "__main__":
    main()
