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

        timelines = []
        lists = []

        if 'available_lists' in state:
            _lists = state['available_lists']
            for l in _lists:
                if '.' in l:
                    (a, n) = l.split('.')
                    name = ' '.join([ e.capitalize() for e in n.split('_')])
                    lists += [ '    ' + name ]
                else:
                    line = ' '.join([ e.capitalize() for e in l.split('_')])
                    lines += [ '  ' + line ]

        lines += timelines
        if lists:
            lines += ['']
            lines += ['  Lists:']
            lines += lists

        return [ line.ljust(20) for line in lines ]
