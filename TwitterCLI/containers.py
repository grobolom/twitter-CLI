from TwitterCLI.views import Timeline, ScrollBar

class TweetWindow():
    """
    Our first container. Trying this out to better handle passing
    down state through the heirarchy to views that are more complex
    """
    def __init__(self, view=Timeline()):
        self.view = view

    def render(self, state):
        _w            = state['screen_width']
        _h            = state['screen_height']
        selected_list = state['selected_list']
        cursor        = state['lists'][ selected_list ]['cursor']

        if selected_list in state['lists']:
            tweets = state['lists'][ selected_list ]['tweets']
        else:
            tweets = []

        # TODO: move this decision making to somewhere up top. We need
        # a good way to decide what size screens should be without
        # hard coding it here in containers
        return self.view.render(tweets, cursor, _w - 22, _h - 1)

class VerticalScrollBar():
    def __init__(self, view=ScrollBar()):
        self.view = view

    def render(self, state):
        height = state['screen_height'] - 1
        cursor = state['cursor']
        c_max = state['cursor_max']
        page = state['screen_height'] - 1

        return self.view.render(height, cursor, c_max, page)
