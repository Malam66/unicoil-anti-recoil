@echo off
title System Download Manager Installer
echo Installing System Download Manager...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Run the application
echo.
echo Starting System Download Manager...
echo.
SystemDownloadManager.exe

pause
