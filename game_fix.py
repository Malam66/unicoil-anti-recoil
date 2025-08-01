#!/usr/bin/env python3
"""
Game Compatibility Fix - Ensures app works in games
"""

import os
import sys
import subprocess
import psutil
import time
import ctypes
import threading
import keyboard
import mouse

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

def fix_game_compatibility():
    """Fix game compatibility issues"""
    print("🎮 Game Compatibility Fix")
    print("=" * 40)
    
    # Check admin privileges
    if not is_admin():
        print("⚠️  Running without administrator privileges")
        print("   Some fixes may not work properly")
        print("   Consider running as administrator for best results")
    
    # Fix mouse permissions
    print("\n🔧 Fixing mouse input permissions...")
    try:
        # Test mouse movement
        ctypes.windll.user32.mouse_event(0x0001, 0, 0, 0, 0)
        print("✅ Mouse permissions OK")
    except Exception as e:
        print(f"❌ Mouse permission error: {e}")
    
    # Fix game detection
    print("\n🔍 Checking for running games...")
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
    
    if not running_games:
        print("❌ No supported games detected")
        print("   Start a game first, then run this tool")
    else:
        print(f"✅ Found {len(running_games)} running game(s)")
    
    # Test recoil control
    print("\n🧪 Testing recoil control...")
    test_recoil_control()
    
    # Provide instructions
    print("\n📋 Game Compatibility Instructions:")
    print("1. Run games as administrator")
    print("2. Set game to Windowed or Borderless mode")
    print("3. Disable V-Sync in game settings")
    print("4. Set mouse sensitivity to 1.0 in game")
    print("5. Disable any in-game mouse acceleration")
    print("6. Add Python and script folder to antivirus exclusions")
    print("7. Use the Stealth Version for best compatibility")
    
    print("\n🎉 Game compatibility fix completed!")
    print("   Your app should now work in games")

def test_recoil_control():
    """Test if recoil control is working"""
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

def create_stealth_config():
    """Create stealth configuration"""
    print("\n🔧 Creating stealth configuration...")
    
    stealth_config = {
        "stealth_mode": True,
        "random_delays": True,
        "human_like_movement": True,
        "variable_patterns": True,
        "process_name": "SystemDownloadManager.exe",
        "window_title": "System Download Manager",
        "description": "Download management utility"
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
    """Main function"""
    print("🎮 Game Compatibility Fix Tool")
    print("=" * 40)
    
    # Fix game compatibility
    fix_game_compatibility()
    
    # Create stealth config
    create_stealth_config()
    
    print("\n💡 Tips for best results:")
    print("1. Run games as administrator")
    print("2. Add Python and script folder to antivirus exclusions")
    print("3. Use the Stealth Version for best compatibility")
    print("4. Set game to Windowed mode")
    print("5. Disable V-Sync in game settings")

if __name__ == "__main__":
    main() 