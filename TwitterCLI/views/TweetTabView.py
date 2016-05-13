import TwitterCLI.colors as colors

class TweetTabView():
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
            _lists = state['lists'].keys()
            for l in _lists:
                print(l)
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
