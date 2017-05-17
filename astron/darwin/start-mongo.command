#!/bin/sh
cd "`dirname "$0"`"
cd ..

mongod --dbpath MongoDB/astrondb
