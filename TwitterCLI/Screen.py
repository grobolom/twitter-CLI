import os

# not able to unit test this right now - not sure how to intercept
# print() in a way that keeps this working correctly
class Screen:
    def render(self, term, rendered_views):
        """
        render all of the views passed in here

        :arg Terminal term: a terminal that we can swing around
        :arg list views: a list of tuples (x_position, y_position, view)
            moves the terminal to each spot and prints the lines to that
            portion of the screen
        """
        os.system('cls')
        term.move(0, 0)
        for view in rendered_views:
            x = view[0]
            y = view[1]
            lines_to_print = view[2]

            i = 0
            for line in lines_to_print:
                with term.location(x, y + i):
                    print('|' + line + '|')
                i += 1
        term.move(0, 0)
