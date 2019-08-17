import click


@click.group()
def i3_autoconfig():
    pass


@i3_autoconfig.command(help="Loads theme from given .toml file.")
@click.argument("theme_path")
@click.option(
    "--backup/--no-backup", help="Generates backup files for dotfiles.", default=True
)
def load(theme_path, backup):
    from .theme import Theme

    theme = Theme(theme_path)
    print("Applying theme: ", theme.name)
    theme.apply_theme(backup=backup)


def main():
    i3_autoconfig()


if __name__ == "__main__":
    main()
