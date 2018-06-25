@echo off
cd ../../
title Uberdog

rem Check to see what version of Panda the user has:
if exist C:\Panda3D-1.10.0-x64 (
    echo 64 bit Panda detected!
    set /P PPYTHON_PATH=<PPYTHON_PATH_X64
) else if exist C:\Panda3D-1.10.0 (
    echo 32 bit Panda detected!
    set /P PPYTHON_PATH=<PPYTHON_PATH
)

rem Define some constants for our UberDOG server:
set MAX_CHANNELS=999999
set STATESERVER=4002
set ASTRON_IP=127.0.0.1:7199
set EVENTLOGGER_IP=127.0.0.1:7197

rem Get the user input:
set /P BASE_CHANNEL="Base channel (DEFAULT: 1000000): " || ^
set BASE_CHANNEL=1000000

echo ===============================
echo Starting Project Altis UberDOG server...
echo ppython: %PPYTHON_PATH%
echo Base channel: %BASE_CHANNEL%
echo Max channels: %MAX_CHANNELS%
echo State Server: %STATESERVER%
echo Astron IP: %ASTRON_IP%
echo Event Logger IP: %EVENTLOGGER_IP%
echo ===============================


%PPYTHON_PATH% -m pip install -r requirements.txt
:main
%PPYTHON_PATH% -m toontown.uberdog.ServiceStart --base-channel %BASE_CHANNEL% ^
               --max-channels %MAX_CHANNELS% --stateserver %STATESERVER% ^
               --astron-ip %ASTRON_IP% --eventlogger-ip %EVENTLOGGER_IP%
goto main
