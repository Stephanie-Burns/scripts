# Scripts
- [makeproject.py](#make-project)
- [OpenGitBash.reg](#open-git-bash)

## Make Project
Create a generic directory structure for python projects.

Relevant file: makeproject.py

```
Directory Structure
.
└── project_name/
    ├── deprecated/
    ├── docs/
    │   └── dev_log.md
    ├── src/
    │   └── test.py
    ├── .gitignore
    └── readme.md

```
For best results assign calling the script to an alias.

```Bash
alias mkpro='python full_path_to_makeproject.py'
```

To write in the current working directory: provide the *name* of your project.

```Bash
mkpro test
````

To write to a specific directory: provide your project *name* and *desired path*.

```Bash
mkpro test c:/parent_directory_for_your_project
````

## Open Git Bash
Windows 11 changed the context menu to be more "friendly" this will change it back.

Relevant file: OpenGitBash.reg

Adds an option to the Windows File Explorer context menu which opens git bash in the **current directory**. This will also set the context menu to show all items by default.

![context_menu](https://user-images.githubusercontent.com/87616660/185630892-e914b39f-89a0-49c4-9c26-92a99853f835.png)

To execute: double click OpenGitBash.reg and the script will write the necessary registry keys.

