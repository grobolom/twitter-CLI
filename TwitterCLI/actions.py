class KeyboardEventHandler:
    def getAction(self, key):
        simple_actions = self._simpleActions()
        if key in simple_actions:
            return simple_actions[ key ]
        return { 'name' : 'None' }

    def _simpleActions(self):
        return {
            'k': { 'name': 'CURSOR_MOVE', 'amount' : -1 },
            'j': { 'name': 'CURSOR_MOVE', 'amount' : 1 },
            'u': { 'name': 'CURSOR_MOVE', 'amount' : -10 },
            'd': { 'name': 'CURSOR_MOVE', 'amount' : 10 },
            'KEY_TAB': { 'name': 'SWITCH_TAB', },
        }
