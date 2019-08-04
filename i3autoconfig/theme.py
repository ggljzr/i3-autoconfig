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

    def __init__(self, data):
        self.colors = dict()
        for c in COLORS:
            self.colors[c] = data["colors"][c]


# tuples with default values
I3_WINDOWS = [
    ("focused", "darkGreen"),
    ("inactive", "darkGrey"),
    ("unfocused", "darkGrey"),
    ("urgent", "darkRed"),
    ("foreground", "foreground"),
]


class I3Config:
    """
    Class representing i3wm settings for given theme. Loaded from ``theme.toml``.
    """

    def __init__(self, data, color_scheme):

        color_pattern = re.compile(r"^#[a-fA-F0-9]{6}$")

        self.window_settings = dict()
        for w in I3_WINDOWS:
            name, default_color = w

            try:
                color = data["i3"]["windows"][name]
            except KeyError:
                color = default_color

            if color_pattern.match(color):
                self.window_settings["name"] = color
            else:
                self.window_settings["name"] = color_scheme.colors["color"]


class Theme:
    def __init__(self, theme_path):
        with open(theme_path, "r") as theme_file:
            data = toml.load(theme_file)

        self.color_scheme = ColorScheme(data)
        self.i3_config = I3Config(data, self.color_scheme)
