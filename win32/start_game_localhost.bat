@echo off
cd ../

rem Check to see what version of Panda the user has:
if exist C:\Panda3D-1.10.0-x64 (
    echo 64 bit Panda detected!
    set /P PPYTHON_PATH=<PPYTHON_PATH_X64
) else if exist C:\Panda3D-1.10.0 (
    echo 32 bit Panda detected!
    set /P PPYTHON_PATH=<PPYTHON_PATH
)

rem Get the user input:
set /P ttUsername="Username: "

rem Get the user input:
set /P ttPassword="Password: "

rem Export the environment variables:
set TT_PLAYCOOKIE=%ttUsername%
set TT_USERNAME=%ttUsername%
set TT_PASSWORD=%ttPassword%
set TT_GAMESERVER=127.0.0.1
set model-path=resources

echo ===============================
echo Starting DubitTown...
echo ppython: %PPYTHON_PATH%
echo Username: %ttUsername%
echo Gameserver: %TT_GAMESERVER%
echo ===============================

:goto

%PPYTHON_PATH% -m toontown.toonbase.ClientStartDist
pause

goto :goto