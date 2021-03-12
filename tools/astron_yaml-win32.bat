@echo off
cd "../astron/"
title Project Altis Astron
mode con: cols=60 lines=20

:start
astrond --loglevel info config/cluster-yaml.yml
PAUSE
goto start
