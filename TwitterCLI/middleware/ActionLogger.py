import asyncio
import logging

class ActionLogger:
    def __init__(self, fname):
        self.filename = fname
        logging.basicConfig(filename=fname, level=logging.INFO)

    @asyncio.coroutine
    def handleAction(self, state, action):
        logging.info(self._getThinObject(action))

    def _getThinObject(self, obj):
        output = {}
        for key, value in obj.items():
            if type(value) == list:
                output[key] = 'list of length ' + str(len(value))
            elif type(value) == list:
                output[key] = 'tuple of size ' + str(len(value))
            elif type(value) == dict:
                output[key] = 'dict with ' + str(len(value)) + ' elements'
            else:
                output[key] = value
        return output
