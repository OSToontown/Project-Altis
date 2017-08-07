@echo off
cd ../

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P ttUsername="Username: "
set /P TT_GAMESERVER="Gameserver (DEFAULT: 167.114.28.238): " || ^
set TT_GAMESERVER=167.114.28.238
set model-path=../resources

rem Export the environment variables:
set ttPassword=password
set TT_PLAYCOOKIE=%ttaUsername%

echo ===============================
echo Starting Toontown Project Altis...
echo ppython: %PPYTHON_PATH%
echo Username: %ttUsername%
echo Gameserver: %TT_GAMESERVER%
echo ===============================

:goto

%PPYTHON_PATH% -m toontown.toonbase.ClientStart
pause

goto :goto