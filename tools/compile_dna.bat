@echo off
cd ../

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

%PPYTHON_PATH% -m tools.compileDNA --logfile packerlog.txt --verbose toontown_central_sz.dna toontown_central_sz.dna
pause