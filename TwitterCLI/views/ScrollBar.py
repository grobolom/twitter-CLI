class ScrollBar:
    def render(self, height, cursor, c_max, page_height):
        cursor_size  = int(height * (page_height / c_max))
        cursor_start = int(height * (cursor / c_max))
        cursor_end   = cursor_start + cursor_size

        left      = [ " " for e in range(0, cursor_start) ]
        scrollbar = [ chr(9608) for e in range(0, cursor_size) ]
        right     = [ " " for e in range(cursor_end, height) ]

        return left + scrollbar + right
