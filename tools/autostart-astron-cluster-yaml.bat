@echo off
cd "../astron/"
title Project Altis Astron

:start
astrond --loglevel info config/cluster-yaml.yml
PAUSE
goto start
