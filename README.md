#Autoconfig script for i3 and other programs

In python3, configs and color themes in toml.

##custom template
Custom template can be added by:

1. Add custom template in template folder
2. Add add template_name in TEMPLATES list in autoconfig.py
3. Add target path (template_name = "/path/to/actual/config") to config.toml (paths section)

Note thath template_name in TEMPLATES and in config.toml must be same. This should be enough to use colors and font setting from theme. In your template use ##colorName## tags to specify color (e.g. ##darkBlue## or ##foreground##) and ##font_family##, ##font_size## for fonts.

##todo
firefox config probably needs foreground and background options for urlbar and toolbar
(maybe use list of colors, check length), error handling, maybe also write list of used tags and unify notation.
