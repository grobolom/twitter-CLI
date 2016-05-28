class Store:
    def __init__(self, reducers, initialState):
        self.reducers = reducers
        self.state = initialState

    def getState(self):
        return self.state
