@echo off

Echo Building Toontown Advance...

cd ../

nuitka --standalone --verbose --recurse-all --enhanced --output-dir=build --python-version=2.7 toontown/toonbase/ClientStart.py
pause