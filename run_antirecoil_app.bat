@echo off
echo Starting UniCoil Anti-Recoil Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

REM Run the launcher
echo Starting launcher...
python launcher.py

pause 