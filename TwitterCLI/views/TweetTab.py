import TwitterCLI.colors as colors

class TweetTab:
    def render(self, state):
        lines = []

        header = [
            colors.title('TwitterCLI'.ljust(20)),
            colors.user('@grobolom'.ljust(20)),
            '',
        ]

        lines += header

        selected = ''
        if 'selected_list' in state:
            selected = state['selected_list']

        if 'lists' in state:
            _lists = self._listOrder(state)
            for l in _lists:
                if '.' in l:
                    (a, n) = l.split('.')
                    name = ' '.join([ e.capitalize() for e in n.split('_')])
                    result = '    ' + name
                else:
                    line = ' '.join([ e.capitalize() for e in l.split('_')])
                    result = '  ' + line

                if l == selected:
                    result = colors.selected(result.ljust(20))

                lines += [ result.ljust(20) ]

        return [ line.ljust(20) for line in lines ]

    def _listOrder(self, state):
        order = [
            'home_timeline',
            'tweets',
        ]

        other_lists = []
        keys = state['lists'].keys()
        for key in keys:
            if key not in other_lists and key not in order:
                other_lists += [ key ]
        return order + sorted(other_lists)
