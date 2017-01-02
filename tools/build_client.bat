@echo off

Echo Building Toontown Advance...

cd ../

nuitka --standalone --recurse-all --verbose --enhanced --output-dir=build --python-version=2.7 toontown/toonbase/ClientStart.py
pause