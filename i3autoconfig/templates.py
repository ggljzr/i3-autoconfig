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
