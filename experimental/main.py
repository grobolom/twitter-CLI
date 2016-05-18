from blessed import Terminal
import asyncio
import time
from queue import Queue
from concurrent.futures import ProcessPoolExecutor

def echoer():
    time.sleep(1)
    return 'bacon'

@asyncio.coroutine
def terminal_process(some_queue):
    while True:
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, echoer)
        x = yield from future
        print(x)

def main():
    loop = asyncio.get_event_loop()
    some_queue = asyncio.Queue()
    asyncio.async(terminal_process(some_queue))

    try:
        loop.run_forever()
    except:
        loop.stop()
    finally:
        loop.close()
        print('!' + some_queue.get_nowait())
    pass

if __name__ == "__main__":
    main()
