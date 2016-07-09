import pytoml as toml
import sys
import subprocess
import re

config = []
theme = []

COLORS = ['black', 'darkGrey', 'darkRed', 'red', 'darkGreen', 'green', 
        'darkYellow', 'yellow', 'darkBlue', 'blue', 'darkMagenta', 'magenta', 
        'cyan', 'darkCyan', 'lightGrey', 'white', 'foreground', 'background']

I3_WINDOWS = ['focused', 'inactive', 'unfocused', 'urgent', 'foreground']

TEMPLATES = ['i3config', 'xresources']

with open('config.toml', 'rb') as config_file:
    config = toml.load(config_file)

argv = sys.argv
argc = len(argv)

if argc < 2:
    print("enter theme path")
    sys.exit()

theme_path = argv[1]

with open(theme_path, 'rb') as theme_file:
    theme = toml.load(theme_file)


#creating temp files and color config
for template in TEMPLATES:

    template_path = 'templates/{}'.format(template)
    template_name = '{}.temp'.format(template)

    print("Template {}".format(template))
    print(template_path)
    print(template_name)
    print("")


    #create temp file
    subprocess.call(['cp', template_path, template_name])

    for color in COLORS:
        color_val = theme['colors'][color]
        #print("{} : {}".format(color, color_val)) 
        subprocess.call(['sed', '-i', 's/##{}##/{}/'.format(color, color_val),template_name])

#additional i3 config block
#i3 windows conf
for window in I3_WINDOWS:
    color = theme['i3']['windows'][window]
    color_pattern = re.compile(r'^#[a-fA-F0-9]{6}$') 

    if color_pattern.match(color):
        color_val = color
    else:
        color_val = theme['colors'][color]
    
    print("{} {} {}".format(window, color, color_val))
    subprocess.call(['sed', '-i', 's/##i3_{}##/{}'.format(window, color_val)], 'i3config.temp')

#gaps conf
border = config['i3']['border']
gaps_inner = config['i3']['gaps-inner']
gaps_outer = config['i3']['gaps-outer']

if gaps_inner == 0 and gaps_outer == 0:
    
    if border == 0:

#coping temp files to their targets
for template in TEMPLATES:
    target_path = config['paths'][template]
    #cp neco
    subprocess.call(['rm', '-f', '{}.temp'.format(template)])
