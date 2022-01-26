"""Console script for py_tutis."""
import sys

import click


@click.command()
def main(args=None):
    """Console script for py_tutis."""
    click.echo("Replace this putting your code into " "py_tutis.cli.main")
    click.echo("documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
