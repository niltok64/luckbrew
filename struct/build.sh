#!/bin/bash
echo "BUILDING DEM CODE"
pip install pyinstaller
mkdir built
pyinstaller main.py --name luck --distpath built --onefile -w
echo "CODE HAS BEEN BUILT YO"
