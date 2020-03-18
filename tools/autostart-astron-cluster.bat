@echo off
cd "../astron/"
title Toontown Stride Astron

:start
astrond --loglevel info config/cluster.yml
PAUSE
goto start