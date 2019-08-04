import toml
import re

COLORS = [
    "black",
    "darkGrey",
    "darkRed",
    "red",
    "darkGreen",
    "green",
    "darkYellow",
    "yellow",
    "darkBlue",
    "blue",
    "darkMagenta",
    "magenta",
    "cyan",
    "darkCyan",
    "lightGrey",
    "white",
    "foreground",
    "background",
]


class ColorScheme:
    """
    Class representing theme's color scheme. This is loaded
    from ``theme.toml`` file.

    Color scheme is represented by 16 colors (bright + dark) as in ``.Xresources``.
    """

    def __init__(self, theme_path):
        with open(theme_path, "r") as theme_file:
            data = toml.load(theme_file)

        self.colors = dict()
        for c in COLORS:
            self.colors[c] = data["colors"][c]

