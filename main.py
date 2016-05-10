import shutil
from TwitterCLI.app import TwitterClient

def main():
    app = TwitterClient()
    app.run(shutil.get_terminal_size())
    return

if __name__ == "__main__":
    main()
