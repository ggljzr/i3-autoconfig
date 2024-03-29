import pytoml
import re
from enum import Enum
import shutil
from pathlib import Path
from importlib.resources import read_text

import subprocess

from i3autoconfig import compton_configs
from .utils import reload_settings

from .templates import (
    XresTemplate,
    I3ConfigTemplate,
    I3BlocksTemplate,
    VSCodeTemplate,
)


class PreflightCheckError(Exception):
    pass


class ColorScheme:
    """
    Class representing theme's color scheme. This is loaded
    from ``theme.toml`` file.

    Color scheme is represented by 16 colors (bright + dark) as in ``.Xresources``.
    """

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

    def __init__(self, data: dict):
        self.colors = dict()
        for c in ColorScheme.COLORS:
            self.colors[c] = data["colors"][c]


class I3Config:
    """
    Class representing i3wm settings for given theme. Loaded from ``theme.toml``.
    """

    # tuples with default values
    I3_WINDOWS = [
        ("focused", "darkGreen"),
        ("inactive", "darkGrey"),
        ("unfocused", "darkGrey"),
        ("urgent", "darkRed"),
        ("foreground", "foreground"),
        ("wborder", None),
    ]

    def __init__(self, data: dict, color_scheme: ColorScheme):

        color_pattern = re.compile(r"^#[a-fA-F0-9]{6}$")

        try:
            self.border = data["i3"]["border"]
        except KeyError:
            self.border = 0

        try:
            self.gaps_inner = data["i3"]["gaps-inner"]
        except KeyError:
            self.gaps_inner = 0

        try:
            self.gaps_outer = data["i3"]["gaps-outer"]
        except KeyError:
            self.gaps_outer = 0

        self.window_settings = dict()
        for w in I3Config.I3_WINDOWS:
            name, default_color = w

            try:
                color = data["i3"]["windows"][name]
            except KeyError:
                color = default_color

            if color is None or color_pattern.match(color):
                self.window_settings[name] = color
            else:
                self.window_settings[name] = color_scheme.colors[color]


class Wallpaper:
    """
    Class representing wallpaper, with path to given picutre and bg mode used in Feh.
    """

    BG_MODES = ["center", "fill", "max", "scale", "tile"]

    def __init__(self, data: dict):
        self.pic = data["wallpaper"]["pic"]

        self.mode = "fill"
        try:
            mode = data["wallpaper"]["mode"]
            if mode in Wallpaper.BG_MODES:
                self.mode = mode
        except KeyError:
            pass

    def apply(self) -> None:
        print("Applying wallpaper: {}".format(self.pic))
        subprocess.call(["feh", "--bg-{}".format(self.mode), self.pic])


class Compton:
    """
    Class representing settings for Compton composition manager.
    """

    SHADOWS = ["mild", "thick", "none"]

    def __init__(
        self,
        data: dict,
        target_path: Path = Path(Path.home(), ".config", "compton.conf"),
    ):
        self.shadows = "none"
        self.target_path = target_path
        try:
            shadows = data["other"]["shadows"]
            if shadows in Compton.SHADOWS:
                self.shadows = shadows
        except KeyError:
            pass

    def apply(self) -> None:
        print("Applying Compton config: {}.conf".format(self.shadows))

        config = read_text(compton_configs, "{}.conf".format(self.shadows))
        with open(self.target_path, "w") as f:
            f.write(config)


class Theme:
    def __init__(self, theme_path: Path):
        with open(theme_path, "r") as theme_file:
            data = pytoml.load(theme_file)

        self.name = data["name"]

        self.color_scheme = ColorScheme(data)
        self.i3_config = I3Config(data, self.color_scheme)
        self.wallpaper = Wallpaper(data)
        self.compton = Compton(data)

        self.templates = [
            XresTemplate(self),
            I3ConfigTemplate(self),
            I3BlocksTemplate(self),
            VSCodeTemplate(self),
        ]

    def preflight_check(self) -> None:
        print("Running theme preflight check...")

        for t in self.templates:
            folder = t.target_folder
            if folder.exists():
                print(
                    "Found target folder for template '{}': {}".format(
                        t.target_name, t.target_folder
                    )
                )
            else:
                raise PreflightCheckError(
                    "Target folder for template '{}' not found at {}".format(
                        t.target_name, t.target_folder
                    )
                )

    def apply_theme(self, backup: bool = False) -> None:
        self.preflight_check()

        for t in self.templates:
            t.apply_template(backup=backup)
        # reload settings
        self.compton.apply()
        self.wallpaper.apply()

        reload_settings()
