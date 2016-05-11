class TweetTabView():
    def render(self, state):
        lines = [
            'TwitterCLI',
            '@grobolom'
        ]

        return [ line.ljust(20) for line in lines ]
