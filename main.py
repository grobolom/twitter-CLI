import shutil
from queue import Queue
from TwitterCLI.app import TwitterClient

def main():
    q = Queue()
    app = TwitterClient(q)
    app.run()
    return

if __name__ == "__main__":
    main()
