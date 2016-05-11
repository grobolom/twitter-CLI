class RootReducer:
    def reduce(self, state, action):
        if action['name'] == 'CURSOR_MOVE':
            return self._cursorMove(state, action)
        return state

    def _cursorMove(self, state, action):
        """
        we use a 'fancy' method to contrain the cursor here - by taking the
        mean of the sorted [0, cursor, cursor_max] we always get the right
        amount. If cursor < 0 or cursor > cursor_max, it moves to the
        extremes of the list and thus we select the correct limit instead
        """

        amount = action['amount']
        cursor = state['cursor'] + amount
        cursor_max = state['cursor_max']
        state['cursor'] = sorted([0, cursor, cursor_max])[1]

        return state
