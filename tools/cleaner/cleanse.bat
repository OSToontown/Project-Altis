@echo off
title Toontown Cleaner

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

%PYTHON_PATH% cleanse.py
pause
exit