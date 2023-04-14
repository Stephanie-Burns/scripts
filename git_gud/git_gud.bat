@echo off

rem get the path of the directory to push from the command line argument
set "directory=%~1"

rem save the current directory
pushd "%CD%"

rem change to the specified directory
cd /d "%directory%"

rem perform the git push operation
@echo on

git add .
if %errorlevel% neq 0 exit /b %errorlevel%
git commit -m "update"
if %errorlevel% neq 0 exit /b %errorlevel%
git push
if %errorlevel% neq 0 exit /b %errorlevel%

@echo off

rem return to starting directory
popd
