@echo off

set /P PPYTHON_PATH=<../PPYTHON_PATH

:main
%PPYTHON_PATH% -m cleanse
pause
goto main