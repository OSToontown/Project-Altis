@echo off
title Project Altis Mongo
cd ../astron

"mongo\Server\3.0\bin\mongod.exe" --dbpath mongo/astrondb
pause
