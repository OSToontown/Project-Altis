@echo off
title Project Altis Mongo
mode con: cols=60 lines=20

cd ../astron

"mongo\Server\3.0\bin\mongod.exe" --dbpath mongo/astrondb
pause
