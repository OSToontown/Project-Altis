@echo off
title Astron
cd ..
astrond --pretty --loglevel debug config/cluster.yml
pause