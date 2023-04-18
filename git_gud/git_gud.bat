@echo off

rem get the path of the directory to push from the command line argument
set "directory=%~1"
pushd "%CD%"
cd /d "%directory%"

git add . && git commit -m "update" && git push

popd