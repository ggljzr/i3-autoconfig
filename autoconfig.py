import pytoml as toml
import sys
import subprocess

config = []
theme = []

COLORS = ['black', 'darkGrey', 'darkRed', 'red', 'darkGreen', 'green', 
        'darkYellow', 'yellow', 'darkBlue', 'blue', 'darkMagenta', 'magenta', 
        'cyan', 'darkCyan', 'lightGrey', 'white']

TEMPLATES = ['i3config', 'xresources']

with open('config.toml', 'rb') as config_file:
    config = toml.load(config_file)

argv = sys.argv()
argc = len(argv)

if argc < 2:
    print("enter theme path")
    sys.exit()

theme_path = argv[1]

with open(theme_path, 'rb') as theme_file:
    theme = toml.load(theme_file)


for template in TEMPLATES:

    for color in COLORS:
        color_val = theme['colors'][color]
