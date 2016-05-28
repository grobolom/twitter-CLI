import copy

class Store:
    def __init__(self, reducers, initialState):
        self.reducers = reducers
        self.state = initialState

    def getState(self):
        return self.state

    def dispatch(self, action):
        new_state = copy.deepcopy(self.state)
        for reducer in self.reducers:
            new_state = reducer.reduce(new_state, action)
        self.state = new_state
