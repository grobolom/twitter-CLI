class RootReducer:
    def reduce(self, state, action):
        if (action == 'CURSOR_UP'):
            if state['cursor'] == 0:
                pass
            else:
                state['cursor'] -= 1
        if (action == 'CURSOR_DOWN'):
            if state['cursor'] == state['cursor_max']:
                pass
            else:
                state['cursor'] += 1
        return state
