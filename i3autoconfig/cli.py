import click


@click.group()
def i3_autoconfig():
    pass


@i3_autoconfig.command(help="Loads theme from given .toml file.")
@click.argument("theme_path")
def load(theme_path):
    from .theme import Theme

    theme = Theme(theme_path)
    print(theme.name)
    print(theme)

    from .templates import I3ConfigTemplate

    i3_config = I3ConfigTemplate()
    print(i3_config.template_path)


def main():
    i3_autoconfig()


if __name__ == "__main__":
    main()
