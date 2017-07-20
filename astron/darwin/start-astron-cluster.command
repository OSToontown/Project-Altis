#!/bin/sh
cd "`dirname "$0"`"
cd ..
./astrond --pretty --loglevel info config/cluster.yml
