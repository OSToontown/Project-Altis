@echo off

Echo Building DubitTown...

cd ../

nuitka --standalone --recurse-all --verbose --enhanced --output-dir=build --python-version=2.7 toontown/toonbase/ClientStartDist.py
pause