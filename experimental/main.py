import asyncio
import time

from blessed import Terminal

def inputter():
    term = Terminal()
    with term.cbreak():
        key = term.inkey(1)
        return key

@asyncio.coroutine
def reader(some_queue):
    while True:
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, inputter)
        x = yield from future
        if x and not x.is_sequence:
            yield from some_queue.put(x)

@asyncio.coroutine
def something_slow(some_queue):
    yield from asyncio.sleep(10)
    yield from some_queue.put('WHAT')

@asyncio.coroutine
def terminal_process(some_queue):
    asyncio.async(reader(some_queue))
    asyncio.async(something_slow(some_queue))
    while True:
        x = yield from some_queue.get()
        print(x)

def main():
    loop = asyncio.get_event_loop()
    some_queue = asyncio.Queue()

    try:
        loop.run_until_complete(terminal_process(some_queue))
    finally:
        loop.close()
        x = some_queue.get()
    pass

if __name__ == "__main__":
    main()
