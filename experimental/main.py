import asyncio
import time

def echoer():
    time.sleep(1)
    return 'bacon'

@asyncio.coroutine
def reader(some_queue):
    while True:
        yield from asyncio.sleep(1)
        yield from some_queue.put('bacon')

@asyncio.coroutine
def terminal_process(some_queue):
    asyncio.async(reader(some_queue))
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
        print(x)
    pass

if __name__ == "__main__":
    main()
