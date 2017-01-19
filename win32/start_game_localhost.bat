@echo off
cd ../

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set /P ttUsername="Username: "

rem Get the user input:
set /P ttaPassword="Password: "

rem Export the environment variables:
<<<<<<< HEAD
set TT_PLAYCOOKIE=%ttUsername%
set TT_GAMESERVER=127.0.0.1
=======
set TTA_USERNAME=%ttaUsername%
set TTA_PASSWORD=%ttaPassword%
set TTA_GAMESERVER=127.0.0.1
>>>>>>> parent of b49fd7e... Devs shouldn't have to connect to the LIVE server to play localhost

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