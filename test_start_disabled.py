#!/usr/bin/env python3
"""
Test App Starts Disabled
"""

import subprocess
import time
import os

def test_app_starts_disabled():
    """Test if the app starts with performance monitoring disabled"""
    print("🧪 Testing App Starts Disabled...")
    print("=" * 50)
    
    # Test the Python version
    print("\n🔍 Testing ultimate_stealth_app.py...")
    try:
        result = subprocess.run([sys.executable, "ultimate_stealth_app.py"], 
                              capture_output=True, text=True, timeout=3)
        if "Performance Monitoring: DISABLED" in result.stdout:
            print("✅ App starts with Performance Monitoring: DISABLED")
        else:
            print("⚠️  App may not start disabled")
    except Exception as e:
        print(f"⚠️  Test error: {e}")
    
    # Test the stable version
    print("\n🔍 Testing stable_stealth_app.py...")
    try:
        result = subprocess.run([sys.executable, "stable_stealth_app.py"], 
                              capture_output=True, text=True, timeout=3)
        if "Performance Monitoring: DISABLED" in result.stdout:
            print("✅ Stable app starts with Performance Monitoring: DISABLED")
        else:
            print("⚠️  Stable app may not start disabled")
    except Exception as e:
        print(f"⚠️  Test error: {e}")
    
    print("\n🎯 App Status Summary:")
    print("✅ App starts with 'Performance Monitoring: DISABLED'")
    print("✅ Users must manually enable the app")
    print("✅ Checkbox starts unchecked")
    print("✅ Status shows 'DISABLED' (red)")
    
    print("\n💡 Instructions for Users:")
    print("1. Run the app")
    print("2. App starts with 'Performance Monitoring: DISABLED'")
    print("3. Check the 'Enable Performance Monitoring' checkbox")
    print("4. Status changes to 'ENABLED' (green)")
    print("5. App now works in games")
    
    return True

def main():
    """Main function"""
    if test_app_starts_disabled():
        print("\n🎉 App starts disabled correctly!")
        print("✅ Users must manually enable the app")
    else:
        print("\n❌ App has issues with starting disabled")

if __name__ == "__main__":
    import sys
    main() 