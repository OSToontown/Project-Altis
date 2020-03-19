@echo off
cd ..
title Project Altis Pip Packages Installer

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

%PYTHON_PATH% -m pip install -r requirements.txt

PAUSE
goto main
