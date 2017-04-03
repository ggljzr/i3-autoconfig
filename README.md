#Autoconfig script for i3 and other programs

In python3, configs and color themes in toml.

##Requirements
* Python3
* pytoml

## Notes

* [xbright](https://github.com/snobb/xbright) is used to set backlight, it has to be modified slightly to return brightness value when no argument is given. This is because * xbacklight * stopped working on Ubuntu with newer kernels. Alternatively you can write a scrpit using `/sys/class/backlight` to set/get brightness.
* There is a bug in [i3blocks](https://github.com/vivien/i3blocks) volume script, causing it to not recognise that pulse audio mixer (on Xubuntu) is used. Workaround is to hardcode pulse option into the script with `MIXER="pulse"`.
* You need account and API key from [Openweathermap](https://home.openweathermap.org) to use `weatherBar.py` script.
* Use [compton](https://github.com/chjj/compton) as compositor. (Optional)
* Use [i3gaps](https://github.com/Airblader/i3) fork. (Optional)
* Custom scripts and dotfiles are [here](https://github.com/ggljzr/i3config) (wildly unorganized).

## Custom template
Custom template can be added by:

1. Add custom template to template folder
2. Add add template_name to TEMPLATES list in autoconfig.py
3. Add target path (template_name = "/path/to/actual/config") to config.toml (paths section)

Note thath template_name in TEMPLATES and in config.toml must be same. This should be enough to use colors and font setting from theme. In your template use ##colorName## tags to specify color (e.g. ##darkBlue## or ##foreground##) and ##font_family##, ##font_size## for fonts.

## TODO
* firefox config probably needs foreground and background options for urlbar and toolbar (maybe use list of colors, check length), error handling, maybe also write list of used tags and unify notation.
* foreground color settings for vim

