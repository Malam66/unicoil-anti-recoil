#!/usr/bin/env python3
"""
Test script to verify all components are working correctly
"""

import sys
import os
import importlib

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    modules = [
        'tkinter',
        'keyboard', 
        'mouse',
        'PIL',
        'psutil',
        'json',
        'threading',
        'time'
    ]
    
    for module in modules:
        try:
            importlib.import_module(module)
            print(f"OK - {module}")
        except ImportError as e:
            print(f"FAILED - {module}: {e}")
            return False
    
    return True

def test_files():
    """Test if all required files exist"""
    print("\nTesting files...")
    
    files = [
        'anti_recoil_app.py',
        'enhanced_antirecoil_app.py',
        'universal_antirecoil_app.py',
        'launcher.py',
        'requirements.txt',
        'pubg_weapons.json',
        'enhanced_no_recoil.lua',
        'simple_no_recoil.lua',
        'run_antirecoil_app.bat'
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"OK - {file}")
        else:
            print(f"MISSING - {file}")
            return False
    
    return True

def test_app_creation():
    """Test if the applications can be created without errors"""
    print("\nTesting application creation...")
    
    try:
        import tkinter as tk
        from anti_recoil_app import AntiRecoilApp
        
        # Create a test window
        root = tk.Tk()
        root.withdraw()  # Hide the window
        app = AntiRecoilApp(root)
        root.destroy()
        print("OK - Basic app creation")
        
        # Test enhanced app
        from enhanced_antirecoil_app import EnhancedAntiRecoilApp
        root = tk.Tk()
        root.withdraw()  # Hide the window
        app = EnhancedAntiRecoilApp(root)
        root.destroy()
        print("OK - Enhanced app creation")
        
        # Test universal app
        from universal_antirecoil_app import UniversalAntiRecoilApp
        root = tk.Tk()
        root.withdraw()  # Hide the window
        app = UniversalAntiRecoilApp(root)
        root.destroy()
        print("OK - Universal app creation")
        
        return True
        
    except Exception as e:
        print(f"FAILED - App creation: {e}")
        return False

def main():
    """Run all tests"""
    print("UniCoil Deployment Test")
    print("=" * 40)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test files
    if not test_files():
        all_passed = False
    
    # Test app creation
    if not test_app_creation():
        all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("SUCCESS - All tests passed! Deployment is ready!")
        print("\nTo run the application:")
        print("1. Double-click 'run_antirecoil_app.bat'")
        print("2. Or run: python launcher.py")
        print("3. Or run: python universal_antirecoil_app.py (RECOMMENDED)")
        print("4. Or run: python anti_recoil_app.py")
        print("5. Or run: python enhanced_antirecoil_app.py")
    else:
        print("FAILED - Some tests failed. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    main() 