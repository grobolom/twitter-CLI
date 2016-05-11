import TwitterCLI.utils.terminal_colors as colors

USER     = colors.GREEN
LINK     = colors.LIGHT_BLUE
MENTION  = colors.LIGHT_YELLOW
HASHTAG  = colors.LIGHT_PURPLE
TITLE    = colors.GREEN
SELECTED = colors.BLACK_ON_WHITE

def color(string, color):
    return color + string + colors.ENDC

def user(string):
    return color(string, USER)

def link(string):
    return color(string, LINK)

def mention(string):
    return color(string, MENTION)

def hashtag(string):
    return color(string, HASHTAG)

def title(string):
    return color(string, TITLE)

def selected(string):
    return color(string, SELECTED)
