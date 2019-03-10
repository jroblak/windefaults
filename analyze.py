"""
Takes a list of process or service names, and (optionally) a Windows version,
and outputs the processes or services which are not installed by default
on that version
"""
import csv
from pathlib import Path

import click

DEFAULTS_PATH = "defaults"
DEFAULTS_EXT = ".csv"
DEFAULTS_FILES = {
    "10": "windows-10-",
    "2008": "server-2008-",
    "2012": "server-2012-",
    "2016": "server-2016-",
    "2019": "server-2019-",
}


def get_defaults_file_path(item_type: str, version: str) -> str:
    file_prefix = DEFAULTS_FILES[version]
    rel_path = file_prefix + item_type + DEFAULTS_EXT
    return Path(DEFAULTS_PATH) / rel_path


def get_defaults(defaults_path: str) -> set:
    defaults: list = []
    with open(defaults_path) as defaults_file:
        reader = csv.reader(defaults_file, delimiter=',', quotechar='"')
        next(reader, None)  # skip the comment
        next(reader, None)  # skip the headers
        for row in reader:
            defaults.append(row[0])

    return set(defaults)


def get_items_to_analyze(file_path: str) -> set:
    items: list = []
    with open(file_path) as analyze_file:
        try:
            reader = csv.reader(analyze_file, delimiter=',', quotechar='"')
        except:
            click.echo("Couldn't parse file - did you pass in a valid CSV?")
            exit()
        for row in reader:
            if "#TYPE" in row[0]:
                continue
            if row[0] == "Name":
                continue
            items.append(row[0])

    return set(items)


def analyze(item_type: str, file_path: str, version: str) -> set:
    defaults_path = get_defaults_file_path(item_type, version)
    defaults = get_defaults(defaults_path)
    analyze_items = get_items_to_analyze(file_path)
    difference = analyze_items - defaults
    return difference


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option("--item_type", type=click.Choice(["services", "processes"]), default="services",
              help="The type of items your analyzing (default: services)")
@click.option("--version", type=click.Choice(["2008", "2012", "2016", "2019", "10"]),
              default="10", help="The version of Windows you're analyzing (default: 10)")
def main(file_path, item_type, version):
    difference = analyze(item_type, file_path, version)
    if len(difference):
        click.echo(f"The following non-default {item_type} were found:")
        for item in difference:
            click.echo(f"[+] {item}")
    else:
        click.echo(f"No non-default {item_type}!")


if __name__ == "__main__":
    main()
