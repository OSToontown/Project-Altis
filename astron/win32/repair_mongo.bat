@echo off
title Altis Development Mongo
cd ..

:main
"MongoDB\Server\3.0\bin\mongod.exe" --dbpath MongoDB/astrondb --repair


pause
