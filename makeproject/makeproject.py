#!/usr/bin/python

"""
Directory Structure
.
└── project_name/
    ├── deprecated/
    │   └── test.py
    ├── docs/
    │   └── dev_log.md
    ├── src/
    │   └── main.py
    ├── .gitignore
    └── readme.md
"""

from pathlib import Path
import argparse
import inspect

import filetemplate


def get_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description=f"Create a boilerplate directory for a python project.\n\n"
    )

    parser.add_argument(
        "name",
        type=str,
        help="The name of your project. Ex: my_app"
    )

    parser.add_argument(
        "dir",
        nargs='?',
        type=Path,
        default=Path.cwd(),
        help=(
            "Optional: The directory in which to place the project. "
            "If no directory is given, the current directory will "
            "be selected."
        )
    )

    return parser.parse_args()


def make_dirs(directories: dict[str, Path]) -> None:

    for directory in directories.values():

        try:
            directory.mkdir(parents=True, exist_ok=True)

        except OSError as e:
            print(f"[ERROR] Failed to write: {directory}")
            print(e)


def make_files(files: dict[str, Path]) -> None:

    for file in files.values():

        try:
            file.touch()

        except OSError as e:
            print(f"[ERROR] Failed to write: {file}")
            print(e)


def make_templates(templates: dict[str, tuple[Path, str]]) -> None:

    for path, template in templates.values():

        try:
            with open(path, 'w') as file_handle:
                file_handle.write(inspect.cleandoc(template))

        except OSError as e:
            print(f"[ERROR] Failed to write: {path}")
            print(e)


def main(args: argparse.Namespace) -> None:

    project_path = args.dir.joinpath(args.name)

    directories = {
        "deprecated"    : project_path.joinpath("deprecated"),
        "docs"          : project_path.joinpath("docs"),
        "src"           : project_path.joinpath("src"),
    }

    files = {
        "gitignore"     : project_path.joinpath(".gitignore"),
        "readme"        : project_path.joinpath("readme.md"),
        "dev_log"       : directories["docs"].joinpath("dev_log.md"),
        "main"          : directories["src"].joinpath("main.py"),
        "test"          : directories["deprecated"].joinpath("test.py"),
    }

    templates = {
        "dev_log"       : (files["dev_log"], filetemplate.DEV_LOG),
        "gitignore"     : (files["gitignore"], filetemplate.GITIGNORE),
    }

    make_dirs(directories)
    make_files(files)
    make_templates(templates)


if __name__ == '__main__':
    args = get_args()
    main(args)
