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

    from .templates import I3config, I3blocks, VSCode

    c = I3config(theme)
    print(c.render())

    b = I3blocks(theme)
    print(b.render())

    v = VSCode(theme)
    print(v.render())


def main():
    i3_autoconfig()


if __name__ == "__main__":
    main()
