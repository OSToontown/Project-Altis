@echo off
cd ..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P ttaUsername="Username: "
set /P ttaPassword="Password: "
set /P TTA_GAMESERVER="Gameserver (DEFAULT: 167.114.28.238): " || ^
set TTA_GAMESERVER=167.114.28.238

echo ===============================
echo Starting Toontown Advance...
echo ppython: %PPYTHON_PATH%
echo Username: %ttaUsername%
echo Gameserver: %TTA_GAMESERVER%
echo ===============================

:goto

%PPYTHON_PATH% -m toontown.toonbase.ClientStart
pause

goto :goto