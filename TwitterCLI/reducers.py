class RootReducer:
    def reduce(self, state, action):
        name = action['name']

        if name:
            state['last_action'] = name

        if name == 'CURSOR_MOVE':
            return self._cursorMove(state, action)
        elif name == 'SWITCH_TAB':
            return self._switchTab(state, action)

        return state

    def _cursorMove(self, state, action):
        """
        we use a 'fancy' method to contrain the cursor here - by taking the
        mean of the sorted [0, cursor, cursor_max] we always get the right
        amount. If cursor < 0 or cursor > cursor_max, it moves to the
        extremes of the list and thus we select the correct limit instead
        """

        amount     = action['amount']
        cursor     = state['cursor'] + amount
        cursor_max = state['cursor_max']

        state['cursor'] = sorted([0, cursor, cursor_max])[1]

        return state

    def _switchTab(self, state, action):
        """
        we also use a fancy method here to find the next tab to switch to
        since we don't want to run off the end, so we stick the zero
        index onto the end and use that to roll back to the start if we
        need to
        """
        current = state['selected_list']
        lists   = state['available_lists']

        if current in lists:
            index      = lists.index(current)
            indices    = list(range(0, len(lists))) + [ 0 ]
            next_index = indices[ index + 1 ]

            state['selected_list'] = lists[next_index]
        else:
            state['selected_list'] = lists[0]

        return state
