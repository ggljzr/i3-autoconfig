#!/usr/bin/python3

import pytoml as toml
import sys
import subprocess
import re

config = []
theme = []

#sed wrapper
def sedw(placeholder, new_string, filename):
    return subprocess.call(['sed', '-i', 's@##{}##@{}@g'.format(placeholder,new_string), filename])


COLORS = ['black', 'darkGrey', 'darkRed', 'red', 'darkGreen', 'green', 
        'darkYellow', 'yellow', 'darkBlue', 'blue', 'darkMagenta', 'magenta', 
        'cyan', 'darkCyan', 'lightGrey', 'white', 'foreground', 'background']

I3_WINDOWS = ['focused', 'inactive', 'unfocused', 'urgent', 'foreground']

TEMPLATES = ['i3config', 'xresources', 'i3blocks']

#shadow presets for compton
SHADOWS = ['mild', 'thick', 'none']

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
        #subprocess.call(['sed', '-i', 's/##{}##/{}/g'.format(color, color_val), template_name])
        sedw(color, color_val, template_name)

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
    #subprocess.call(['sed', '-i', 's/##i3_{}##/{}/g'.format(window, color_val), 'i3config.temp'])
    sedw('i3_' + window, color_val, 'i3config.temp')

#gaps conf
border = theme['i3']['border']
gaps_inner = theme['i3']['gaps-inner']
gaps_outer = theme['i3']['gaps-outer']

if gaps_inner == 0 and gaps_outer == 0:
    
    #remove i3gaps calls
    subprocess.call(['sed', '-i', 's/gaps_inner/##/g', 'i3config.temp'])
    subprocess.call(['sed', '-i', 's/gaps_outer/##/g', 'i3config.temp'])
    
    if border != 0:
        #subprocess.call(['sed', '-i', 's/##border##/{}'.format(border), 'i3config.temp'])
        sedw('border', border, 'i3config.temp')

else:
    sedw('gaps_inner', gaps_inner, 'i3config.temp')
    sedw('gaps_outer', gaps_outer, 'i3config.temp')
    sedw('border', border, 'i3config.temp')

#fonts
for template in TEMPLATES:
    template_name = '{}.temp'.format(template)
    sedw('font_family', theme['other']['font'], template_name)
    sedw('font_size', theme['other']['font-size'], template_name)

#wallpaper
sedw('wallpaper', theme['other']['wallpaper'], 'i3config.temp')

#coping temp files to their targets
for template in TEMPLATES:
    template_name = '{}.temp'.format(template)
    target_path = config['paths'][template]
    subprocess.call(['cp', template_name, target_path])
    subprocess.call(['rm', '-f', template_name])

#copying compton config
shadows = theme['other']['shadows']
if shadows not in SHADOWS:
    print('{} not in compton shadows presets, defaults to none'.format(shadows))
    shadows = 'none'

compton_preset = 'compton_configs/compton.conf.{}'.format(shadows)
#compton does not use any template so copying is done here
subprocess.call(['cp', compton_preset, config['paths']['compton']])

#reload settings
subprocess.call(['xrdb', '-load', config['paths']['xresources']])
subprocess.call(['i3-msg', 'restart'])
subprocess.call(['pkill', 'compton'])
subprocess.call(['compton', '-b'])
subprocess.call(['feh', '--bg-scale', theme['other']['wallpaper']])

