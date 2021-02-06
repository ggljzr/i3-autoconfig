# Autoconfig script for i3 and other programs

In python3, configs and color themes in toml.

## Requirements
* Python3
* toml

## Notes

* [xbright](https://github.com/snobb/xbright) is used to set backlight, it has to be modified slightly to return brightness value when no argument is given. This is because * xbacklight * stopped working on Ubuntu with newer kernels. Alternatively you can write a scrpit using `/sys/class/backlight` to set/get brightness.
* There is a bug in [i3blocks](https://github.com/vivien/i3blocks) volume script, causing it to not recognise that pulse audio mixer (on Xubuntu) is used. Workaround is to hardcode pulse option into the script with `MIXER="pulse"`.
* You need account and API key from [Openweathermap](https://home.openweathermap.org) to use `weatherBar.py` script.
* Use [compton](https://github.com/chjj/compton) as compositor. (Optional)
* Use [i3gaps](https://github.com/Airblader/i3) fork. (Optional)
* Custom scripts and dotfiles are [here](https://github.com/ggljzr/i3config) (wildly unorganized).


## VS Code theme

1. Copy ``autoconfig-theme`` to ``~/.vscode/extensions``
2. Set ``vscode`` path in ``config.toml`` to ``~/.vscode/extensions/autoconfig-theme/theme/autoconfig-theme-color-theme.json``

## Fish config file

Copy to ``~/.config/fish``. This file uses colors from ``.Xresources``, so it does not need a template.
