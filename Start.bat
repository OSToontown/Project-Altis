@echo off
title Project Altis CLI Launcher

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

:menu
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What do you want to do!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo.
echo #1 - Run Project Altis
echo #2 - Install Pip Modules
echo #3 - Exit
echo. 
choice /C:123 /n /m "Selection: "%1
if errorlevel ==3 EXIT /B
if errorlevel ==2 goto pip
if errorlevel ==1 goto run

:run
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What do you want to launch!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo. 
echo #1 - Locally Host a Server
echo #2 - Connect to an Existing Server
echo #3 - Connect to the Official Server
echo #4 - Go Back
echo.
choice /C:1234 /n /m "Selection: "
if errorlevel ==4 goto menu
if errorlevel ==3 goto awsserver
if errorlevel ==2 goto connect
if errorlevel ==1 goto db

:db
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What database do you want to use!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo. 
echo #1 - YAML (Recommended)
echo #2 - MongoDB
echo #3 - Go Back
echo.
choice /C:123 /n /m "Selection: "
if errorlevel ==3 goto run
if errorlevel ==2 goto mongo
if errorlevel ==1 goto yaml

:yaml
cls 
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Starting Localhost!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
cd tools
echo Launching Astron...
START autostart-astron-cluster-yaml.bat
echo Launching the Uberdog Server...
START autostart-uberdog-server.bat
echo Launching the AI Server...
START autostart-ai-server.bat
cd ..
SET TT_GAMESERVER=127.0.0.1
goto game


:mongo
cls 
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Starting Localhost!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
cd tools
echo Launching Mongo...
START autostart-mongo-database.bat
echo Launching Astron...
START autostart-astron-cluster-mongo.bat
echo Launching the Uberdog Server...
START autostart-uberdog-server.bat
echo Launching the AI Server...
START autostart-ai-server.bat
cd ..
SET TT_GAMESERVER=127.0.0.1
goto game

:connect
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo What Server are you connecting to!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
set /P TT_GAMESERVER="Server IP: "
goto game

:awsserver
set TT_GAMESERVER=crankysupertoon.ddns.net

:game
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Username [!] This does get stored in your source code so beware!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
set /P ttUsername="Username: "
set TT_PLAYCOOKIE=%ttUsername%
set TT_USERNAME=%ttUsername%
set TT_PASSWORD=%ttUsername%
echo.
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Welcome to Project Altis, %ttUsername%!
echo The Tooniverse Awaits You!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
:startgame
title Project Altis Client
%PYTHON_PATH% -m toontown.toonbase.ClientStart
PAUSE
goto startgame

:pip
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Installing Pip Packages. This May Take A While!
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
%PYTHON_PATH% -m pip install -r requirements.txt
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Returning to Main Script in 5 seconds
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
timeout /t 1 /nobreak > NUL
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Returning to Main Script in 4 seconds
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
timeout /t 1 /nobreak > NUL
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Returning to Main Script in 3 seconds
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
timeout /t 1 /nobreak > NUL
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Returning to Main Script in 2 seconds
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
timeout /t 1 /nobreak > NUL
cls
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
echo Returning to Main Script in 1 second
echo = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
timeout /t 1 /nobreak > NUL
goto menu
PAUSE