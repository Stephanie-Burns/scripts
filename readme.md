# Scripts
- [makeproject.py](#make-project)
- [OpenGitBash.reg](#open-git-bash)
- [mdtoc.py](#markdown-table-of-contents-generator)
- [git_gud.bat](#git-gud)

## Make Project
Create a generic directory structure for python projects.

Relevant file: makeproject.py

```
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

## Markdown Table of Contents Generator
Iterates over the ##### Headers of a markdown file and returns a formatted
table of contents. By default the output is also appended to the system
clipboard.

| Argument | Argument Short | Required? | Description |
|---|---|---|---|
| path |  | Yes | The relative or absolute path to your markdown file. |
| --alphabetical | -a | No | Output will be alphabetized. |
| --clipboard | -c | No | Output will **NOT** be saved to the clipboard. |
| --output | -o | No | Output will **NOT** be printed to the console. |
| --whitelist | -w | No | Only passed headers will be reported.<br><br>H1 - H6 tags are returned by default.<br><br>Arguments should be passed as integers only. <br><br>For example, to return only H1 and H2  <br>tags you would pass ... -w 1 2 to the script. |ntegers only. <br><br>For example, to return only H1 and H2  <br>tags you would pass ... -w 1 2 to the script. |


For best results assign calling the script to an alias.

```Bash
alias mkpro='python full_path_to_mdtoc.py'
```

## Git Gud
Simple bat file to run the git commit logic on Windows. Intended for use by python scripts to keep execution isolated. Not as good as the API, but good enough for most stuff. 

Make sure git is visible to your path and you have SSH access to GitHub.
