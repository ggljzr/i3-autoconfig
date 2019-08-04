class Template:
    """
    Base class for representing templates.
    """

    def __init__(self, template_path):
        self.template_path = template_path


class I3ConfigTemplate(Template):
    def __init__(self, template_path="templates/i3config"):
        super().__init__(template_path)
        with open(self.template_path, "r") as f:
            print(f.read())
