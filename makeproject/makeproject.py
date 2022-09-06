
from os import getcwd, mkdir
from argparse import ArgumentParser
from pathlib import Path

import filetemplate


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


def get_args():

    parser = ArgumentParser(
        description=f"Create a boilerplate directory for a python project.\n\n"
    )

    parser.add_argument(
        "name",
        type=str,
        help="The name of your project. Ex: my_app"
    )

    parser.add_argument(
        'dir',
        nargs='?',
        default=getcwd(),
        help=("Optional: The directory in which to place the project. "
              "If no directory is given, the current directory will "
              "be used instead.")
    )

    return parser.parse_args()


def make_dirs(
    project_path: str,
    directories: list[str, ...],
    create_parent=True
) -> None:

    try:
        if create_parent:
            mkdir(project_path)

        for directory in directories:
            mkdir(f"{project_path}\\{directory}")

    # TODO Replace base with something useful
    except BaseException as e:
        print(f"[ERROR] Failed to write:  {directory}")
        print(e)


def make_file(path: str, file_name: str) -> None:

    try:
        Path(f"{path}\\{file_name}").touch()

    # TODO Replace base with something useful
    except BaseException as e:
        print(f"[ERROR] Failed to write:  {file_name} to {path}")
        print(e)


def write_file(path: str, text_body: str) -> None:

    try:
        with open(path, "w") as file_handle:
            file_handle.write(text_body)

    # TODO Replace base with something useful
    except BaseException as e:
        print(f"[ERROR] Failed to write: {path}")
        print(e)


def main():

    args = get_args()
    project_name = args.name
    cwd = args.dir

    project_path = f"{cwd}\\{project_name}"
    directories = ["deprecated", "docs", "src"]

    make_dirs(project_path, directories)

    make_file(project_path, "readme.md")
    make_file(f"{project_path}\\deprecated", "test.py")
    make_file(f"{project_path}\\src", "main.py")

    write_file(
        f"{project_path}\\docs\\dev_log.md",
        filetemplate.dev_log_body(project_name)
    )
    write_file(
        f"{project_path}\\.gitignore",
        filetemplate.git_ignore_body()
    )


if __name__ == '__main__':
    main()
