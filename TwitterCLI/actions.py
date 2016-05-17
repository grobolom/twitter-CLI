class KeyboardEventHandler:
    def getAction(self, key, state):
        simple_actions = self._simpleActions()
        if key in simple_actions:
            return simple_actions[ key ]
        if key == 'KEY_ENTER':
            return self._getTweets(state)
        return { 'name' : 'None' }

    def _simpleActions(self):
        return {
            'k': { 'name': 'CURSOR_MOVE', 'amount' : -1 },
            'j': { 'name': 'CURSOR_MOVE', 'amount' : 1 },
            'u': { 'name': 'CURSOR_MOVE', 'amount' : -10 },
            'd': { 'name': 'CURSOR_MOVE', 'amount' : 10 },
            'KEY_TAB': { 'name': 'SWITCH_TAB', },
        }

    def _getTweets(self, state):
        selected_list = state['selected_list']
        current = state['lists'][ selected_list ]
        return {
            'name': 'GET_TWEETS',
            'since': current[0]['id'],
        }
