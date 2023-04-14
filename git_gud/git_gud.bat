@echo off

rem get the path of the directory to push from the command line argument
set "directory=%~1"

rem save the current directory
pushd "%CD%"

rem change to the specified directory
cd /d "%directory%"

rem perform the git push operation
@echo on
git add . & git commit -m "update" & git push

@echo off
popd