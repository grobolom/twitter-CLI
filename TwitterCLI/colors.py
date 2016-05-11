import TwitterCLI.utils.terminal_colors as colors

USER     = colors.GREEN
LINK     = colors.LIGHT_BLUE
MENTION  = colors.LIGHT_YELLOW
HASHTAG  = colors.LIGHT_PURPLE

def color(string, color):
    return color + string + colors.ENDC
