class SplashScreen:
    def render(self, text, width, height):
        text_height = len(text)
        start_at = self._writePos(height, text_height)
        end_at = start_at + text_height

        top_padding = [ " " * width for i in range(0, start_at) ]
        bottom_padding = [ " " * width for i in range(0, height - end_at) ]
        lines = []
        for line in text:
            text_length = len(line)
            start = self._writePos(width, text_length)
            end = start + text_length - 1

            left_padding = " " * start
            right_padding = " " * (width - end - 1)

            lines += [ left_padding + line + right_padding ]

        return top_padding + lines + bottom_padding

    def _writePos(self, c_size, e_size):
        """
        returns a position to start writing at given
        a container size (c_size) and the size of the element to be placed
        inside it (e_size)
        """
        return int(c_size // 2 - e_size // 2)
