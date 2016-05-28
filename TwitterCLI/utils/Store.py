import jsonpickle
import json

class Store:
    """
    simple wrapper for saving our state
    """
    def _saveStore(self, state, filehandle):
        filehandle.write(jsonpickle.encode(state))

    def _loadStore(self, filehandle):
        return jsonpickle.decode(filehandle.read())


