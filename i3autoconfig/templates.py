import jinja2


class Template:
    """
    Base class for representing templates.
    """

    def __init__(self, theme, template_path, target_path):
        self.template_path = template_path
        self.theme = theme
        self.target_path = target_path

        with open(self.template_path, "r") as f:
            self.template = jinja2.Template(f.read())

    def render(self):
        raise NotImplementedError


class XresTemplate(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_path="i3autoconfig/templates/xresources.jinja",
            target_path="~/.Xresources",
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)


class I3config(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_path="i3autoconfig/templates/i3config.jinja",
            target_path="~/.i3/config",
        )

    def render(self):
        i3_config = self.theme.i3_config
        window_settings = i3_config.window_settings

        return self.template.render(
            border=i3_config.border,
            gaps_inner=i3_config.gaps_inner,
            background=self.theme.color_scheme.colors["background"],
            **window_settings
        )


class I3blocks(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_path="i3autoconfig/templates/i3blocks.jinja",
            target_path="~/i3blocks.conf",
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)


class VSCode(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_path="i3autoconfig/templates/vscode.jinja",
            target_path="~/.vscode/extensions/autconfig-theme/themes/autconfig-theme-color-theme.json",
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)
