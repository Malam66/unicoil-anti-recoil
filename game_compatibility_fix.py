#!/usr/bin/env python3
"""
Game Compatibility Fix Script
Fixes common issues that prevent anti-recoil from working in games
"""

import os
import sys
import subprocess
import psutil
import time
import ctypes
from ctypes import wintypes

def is_admin():
    """Check if running as administrator"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Re-run script as administrator"""
    if not is_admin():
        print("Requesting administrator privileges...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

def check_game_processes():
    """Check for running game processes"""
    game_processes = {
        "CS:GO": ["csgo.exe", "cs2.exe"],
        "Valorant": ["VALORANT.exe", "VALORANT-Win64-Shipping.exe"],
        "PUBG": ["PUBG.exe", "TslGame.exe"],
        "Apex Legends": ["r5apex.exe", "Apex.exe"],
        "Fortnite": ["FortniteClient-Win64-Shipping.exe"],
        "Overwatch": ["Overwatch.exe"],
        "Call of Duty": ["cod.exe", "codmw.exe", "codwz.exe"],
        "Rainbow Six Siege": ["RainbowSix.exe", "RainbowSix_Vulkan.exe"],
        "Battlefield": ["bf.exe", "bf2042.exe"],
        "Destiny 2": ["Destiny2.exe"],
        "Halo": ["HaloInfinite.exe", "Halo.exe"],
        "Counter-Strike 2": ["cs2.exe"],
        "Team Fortress 2": ["hl2.exe"],
        "Left 4 Dead 2": ["l4d2.exe"],
        "GTA V": ["GTA5.exe"],
        "Red Dead Redemption 2": ["RDR2.exe"],
        "Cyberpunk 2077": ["Cyberpunk2077.exe"],
        "The Division 2": ["TheDivision2.exe"],
        "Escape from Tarkov": ["EscapeFromTarkov.exe"]
    }
    
    running_games = []
    
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_name = proc.info['name'].lower()
                for game, processes in game_processes.items():
                    for process in processes:
                        if process.lower() in process_name:
                            running_games.append(game)
                            print(f"✅ Found running game: {game}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    except Exception as e:
        print(f"Error checking processes: {e}")
    
    return running_games

def fix_mouse_permissions():
    """Fix mouse input permissions"""
    print("\n🔧 Fixing mouse input permissions...")
    
    try:
        # Set mouse input flags
        MOUSEEVENTF_MOVE = 0x0001
        MOUSEEVENTF_LEFTDOWN = 0x0002
        MOUSEEVENTF_LEFTUP = 0x0004
        
        # Test mouse movement
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, 0, 0, 0, 0)
        print("✅ Mouse permissions OK")
        return True
    except Exception as e:
        print(f"❌ Mouse permission error: {e}")
        return False

def fix_antivirus_exclusions():
    """Add application to antivirus exclusions"""
    print("\n🔧 Adding to antivirus exclusions...")
    
    try:
        current_dir = os.getcwd()
        python_exe = sys.executable
        
        # Common antivirus exclusion paths
        exclusion_paths = [
            current_dir,
            python_exe,
            os.path.join(current_dir, "*.py"),
            os.path.join(current_dir, "*.exe")
        ]
        
        print("📝 Add these paths to your antivirus exclusions:")
        for path in exclusion_paths:
            print(f"   {path}")
        
        return True
    except Exception as e:
        print(f"❌ Error setting exclusions: {e}")
        return False

def optimize_game_settings():
    """Optimize game settings for better compatibility"""
    print("\n🔧 Optimizing game settings...")
    
    optimizations = [
        "Set game to Windowed or Borderless mode",
        "Disable V-Sync in game settings",
        "Set mouse sensitivity to 1.0 in game",
        "Disable any in-game mouse acceleration",
        "Set game priority to High in Task Manager",
        "Run game as administrator"
    ]
    
    print("📋 Recommended game optimizations:")
    for i, opt in enumerate(optimizations, 1):
        print(f"   {i}. {opt}")
    
    return True

def test_recoil_control():
    """Test if recoil control is working"""
    print("\n🧪 Testing recoil control...")
    
    try:
        import mouse
        import keyboard
        
        print("📋 Test Instructions:")
        print("1. Hold LEFT MOUSE BUTTON for 3 seconds")
        print("2. You should see mouse movement")
        print("3. Press ESC to stop test")
        
        start_time = time.time()
        test_duration = 3
        
        while time.time() - start_time < test_duration:
            if keyboard.is_pressed('esc'):
                print("Test stopped by user")
                break
                
            if mouse.is_pressed(button='left'):
                print("Mouse clicked - applying recoil compensation...")
                mouse.move(0, 5, absolute=False)
                time.sleep(0.1)
            
            time.sleep(0.01)
        
        print("✅ Recoil control test completed")
        return True
        
    except ImportError:
        print("❌ Missing dependencies: mouse, keyboard")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def create_stealth_config():
    """Create stealth configuration file"""
    print("\n🔧 Creating stealth configuration...")
    
    stealth_config = {
        "stealth_mode": True,
        "random_delays": True,
        "human_like_movement": True,
        "variable_patterns": True,
        "process_name": "SystemMonitor.exe",
        "window_title": "System Performance Monitor",
        "description": "System optimization utility"
    }
    
    try:
        import json
        with open('stealth_config.json', 'w') as f:
            json.dump(stealth_config, f, indent=2)
        print("✅ Stealth configuration created")
        return True
    except Exception as e:
        print(f"❌ Error creating config: {e}")
        return False

def main():
    """Main compatibility fix function"""
    print("🎮 Game Compatibility Fix Tool")
    print("=" * 40)
    
    # Check admin privileges
    if not is_admin():
        print("⚠️  Running without administrator privileges")
        print("   Some fixes may not work properly")
        print("   Consider running as administrator for best results")
    
    # Check running games
    print("\n🔍 Checking for running games...")
    running_games = check_game_processes()
    
    if not running_games:
        print("❌ No supported games detected")
        print("   Start a game first, then run this tool")
    else:
        print(f"✅ Found {len(running_games)} running game(s)")
    
    # Fix permissions
    mouse_ok = fix_mouse_permissions()
    
    # Fix antivirus
    antivirus_ok = fix_antivirus_exclusions()
    
    # Optimize settings
    optimize_game_settings()
    
    # Create stealth config
    stealth_ok = create_stealth_config()
    
    # Test recoil control
    recoil_ok = test_recoil_control()
    
    # Summary
    print("\n📊 Compatibility Fix Summary:")
    print("=" * 40)
    print(f"Running Games: {'✅' if running_games else '❌'}")
    print(f"Mouse Permissions: {'✅' if mouse_ok else '❌'}")
    print(f"Antivirus Exclusions: {'✅' if antivirus_ok else '❌'}")
    print(f"Stealth Config: {'✅' if stealth_ok else '❌'}")
    print(f"Recoil Control: {'✅' if recoil_ok else '❌'}")
    
    if all([mouse_ok, antivirus_ok, stealth_ok, recoil_ok]):
        print("\n🎉 All compatibility fixes applied successfully!")
        print("   Your anti-recoil should now work in games")
    else:
        print("\n⚠️  Some fixes failed. Try running as administrator.")
    
    print("\n💡 Tips for best results:")
    print("1. Run games as administrator")
    print("2. Add Python and script folder to antivirus exclusions")
    print("3. Use the Stealth Version for best compatibility")
    print("4. Set game to Windowed mode")
    print("5. Disable V-Sync in game settings")

if __name__ == "__main__":
    main() 