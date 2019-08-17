import jinja2
import shutil
from pathlib import Path, PurePath

from importlib.resources import read_text


class BackupFileExists(Exception):
    pass


class Template:
    """
    Base class for representing templates.
    """

    def __init__(self, theme, template_name, target_path):
        self.theme = theme
        self.target_path = target_path

        template_text = read_text(__package__, template_name)
        self.template = jinja2.Template(template_text)

    def render(self):
        raise NotImplementedError

    @property
    def target_folder(self):
        return self.target_path.parent

    @property
    def target_name(self):
        return self.target_path.name

    def apply_template(self, backup=False):
        if backup:
            bak_path = self.target_path.with_suffix(".bak")

            if bak_path.exists:
                raise BackupFileExists(
                    """
                    Backup file for {} already exists.
                    This exception is raised to prevent accidental backup overwrite.
                    Run with '--no-backup' option to prevent overwriting current backup files.
                    """.format(
                        self.target_path
                    )
                )

            shutil.copyfile(self.target_path, bak_path)
        with open(self.target_path, "w") as f:
            f.write(self.render())


class XresTemplate(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_name="xresources.jinja",
            target_path=Path(Path.home(), ".Xresources"),
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)


class I3ConfigTemplate(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_name="i3config.jinja",
            target_path=Path(Path.home(), ".i3", "config"),
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


class I3BlocksTemplate(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_name="i3blocks.jinja",
            target_path=Path(Path.home(), ".i3blocks.conf"),
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)


class VSCodeTemplate(Template):
    def __init__(self, theme):
        super().__init__(
            theme,
            template_name="vscode.jinja",
            target_path=Path(
                Path.home(),
                ".vscode",
                "extensions",
                "autoconfig-theme",
                "themes",
                "autoconfig-theme-color-theme.json",
            ),
        )

    def render(self):
        colors = self.theme.color_scheme.colors
        return self.template.render(**colors)
