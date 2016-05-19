import asyncio
import time
from blessed import Terminal

def inputter():
    term = Terminal()
    with term.cbreak():
        key = term.inkey(1)
        if key and not key.is_sequence:
            return key
        return None

@asyncio.coroutine
def reader(queue):
    while True:
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, inputter)
        key = yield from future
        if key:
            yield from queue.put(key)

@asyncio.coroutine
def our_process(queue):
    while True:
        x = yield from queue.get()
        print(x)

def main():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()
    asyncio.async(reader(queue))
    try:
        loop.run_until_complete(our_process(queue))
    finally:
        loop.close()

if __name__ == "__main__":
    main()
