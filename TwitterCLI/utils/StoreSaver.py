import jsonpickle
import json

class StoreSaver:
    """
    simple wrapper for saving our state
    """
    def saveStore(self, state, filehandle):
        filehandle.write(jsonpickle.encode(state))

    def loadStore(self, filehandle):
        return jsonpickle.decode(filehandle.read())
