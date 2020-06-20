@echo off
cd "../astron/"
title Project Altis Astron

:start
astrond --loglevel info config/cluster.yml
PAUSE
goto start
