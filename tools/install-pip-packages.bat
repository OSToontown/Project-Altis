@echo off
cd ..
title Project Altis Pip Packages Installer

%PYTHON_PATH% -m pip install -r requirements.txt

PAUSE
goto main
