class TweetTabView():
    def render(self, state):
        lines = []

        header = [
            'TwitterCLI',
            '@grobolom',
            '',
        ]

        lines += header

        if 'available_lists' in state:
            _lists = state['available_lists']
            for l in _lists:
                line = ' '.join([ e.capitalize() for e in l.split('_')])
                lines += [ ' ' + line ]

        return [ line.ljust(20) for line in lines ]
