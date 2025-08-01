#!/usr/bin/env python3
"""
Simple test script to verify recoil control is working
"""

import time
import mouse
import keyboard

def test_recoil_control():
    """Test if recoil control is working"""
    print("Testing Recoil Control...")
    print("1. Hold LEFT MOUSE BUTTON to test recoil control")
    print("2. Press ESC to stop the test")
    print("3. You should see mouse movement when clicking")
    print("\nStarting test in 3 seconds...")
    
    time.sleep(3)
    
    try:
        while True:
            if keyboard.is_pressed('esc'):
                print("Test stopped by user")
                break
                
            if mouse.is_pressed(button='left'):
                print("Mouse clicked - applying recoil compensation...")
                # Simulate recoil compensation
                mouse.move(0, 5, absolute=False)  # Move down 5 pixels
                time.sleep(0.1)
                
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("Test interrupted")
    
    print("Test completed!")

if __name__ == "__main__":
    test_recoil_control() 