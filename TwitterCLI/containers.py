from TwitterCLI.views.TimelineView import TimelineView

class TweetWindow():
    """
    Our first container. Trying this out to better handle passing
    down state through the heirarchy to views that are more complex
    """
    def __init__(self, view=TimelineView()):
        self.view = view

    def render(self, state):
        _w            = state['screen_width']
        _h            = state['screen_height']
        cursor        = state['cursor']
        selected_list = state['selected_list']

        if selected_list in state['lists']:
            tweets = state['lists'][ selected_list ]
        else:
            tweets = []

        # TODO: move this decision making to somewhere up top. We need
        # a good way to decide what size screens should be without
        # hard coding it here in containers
        return self.view.render(tweets, cursor, _w - 21, _h - 1)
