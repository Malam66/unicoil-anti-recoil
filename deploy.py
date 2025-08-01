#!/usr/bin/env python3
"""
UniCoil Auto-Deployment Script
Automatically sets up and tests the entire anti-recoil application
"""

import subprocess
import sys
import os
import time

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"SUCCESS - {description}")
            return True
        else:
            print(f"FAILED - {description}")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"FAILED - {description}")
        print(f"Exception: {e}")
        return False

def check_python():
    """Check if Python is installed"""
    print("Checking Python installation...")
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"OK - Python found: {result.stdout.strip()}")
            return True
        else:
            print("FAILED - Python not found or not working")
            return False
    except Exception as e:
        print(f"FAILED - Python check: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    return run_command("pip install -r requirements.txt", "Installing dependencies")

def run_tests():
    """Run the test script"""
    return run_command("python test_deployment.py", "Running deployment tests")

def launch_app():
    """Launch the application"""
    print("\nLaunching UniCoil Application...")
    print("Choose an option:")
    print("1. Launch Launcher (recommended)")
    print("2. Launch Basic App")
    print("3. Launch Enhanced App")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        return run_command("python launcher.py", "Launching launcher")
    elif choice == "2":
        return run_command("python anti_recoil_app.py", "Launching basic app")
    elif choice == "3":
        return run_command("python enhanced_antirecoil_app.py", "Launching enhanced app")
    elif choice == "4":
        print("Goodbye!")
        return True
    else:
        print("Invalid choice")
        return False

def main():
    """Main deployment function"""
    print("UniCoil Auto-Deployment")
    print("=" * 50)
    
    # Check Python
    if not check_python():
        print("\nFAILED - Python is required but not found.")
        print("Please install Python 3.7+ from https://python.org")
        input("Press Enter to exit...")
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("\nFAILED - Failed to install dependencies.")
        input("Press Enter to exit...")
        return False
    
    # Run tests
    if not run_tests():
        print("\nFAILED - Deployment tests failed.")
        input("Press Enter to exit...")
        return False
    
    print("\n" + "=" * 50)
    print("SUCCESS - Deployment completed successfully!")
    print("\nYour UniCoil anti-recoil application is ready to use!")
    
    # Ask if user wants to launch the app
    launch = input("\nWould you like to launch the application now? (y/n): ").strip().lower()
    if launch in ['y', 'yes']:
        launch_app()
    
    print("\nQuick Start Guide:")
    print("1. Double-click 'run_antirecoil_app.bat' for easy launch")
    print("2. Run 'python launcher.py' to choose between versions")
    print("3. Run 'python anti_recoil_app.py' for basic version")
    print("4. Run 'python enhanced_antirecoil_app.py' for enhanced version")
    print("\nRead APP_README.md for detailed instructions")
    
    input("\nPress Enter to exit...")
    return True

if __name__ == "__main__":
    main() 