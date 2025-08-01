# Enhanced Universal No Recoil Script

## Features

### 🎯 **JSON Configuration System**
- External weapon patterns stored in `weapon_config.json`
- Easy to modify and extend weapon patterns
- Organized by game and weapon categories
- No need to edit the main script for new weapons

### 🎮 **Advanced Game Detection**
- Automatically detects popular games:
  - CS:GO / Counter-Strike 2
  - Valorant
  - PUBG
  - Apex Legends
  - Fortnite
  - Overwatch
  - Call of Duty / Warzone
  - Rainbow Six Siege

### 🔫 **Comprehensive Weapon Support**
- **CS:GO**: AK-47, M4A1, AWP, M4A4, FAMAS, Galil
- **Valorant**: Vandal, Phantom, Spectre, Operator, Guardian
- **PUBG**: AKM, M416, SCAR-L, UMP45, M249, DP28
- **Apex**: R-301, Flatline, Spitfire
- **Generic**: Default, Strong Recoil, Weak Recoil patterns

### 🎛️ **Enhanced Controls**
- **F1**: Toggle script on/off
- **F2**: Cycle through weapons
- **F3**: Adjust sensitivity (0.1 - 2.0)
- **F4**: Toggle Logitech mode (smoother movement)
- **F5**: Toggle auto game detection
- **F6**: Toggle randomization (adds variation to patterns)
- **Mouse Wheel**: Cycle weapon categories
- **Left Click**: Trigger recoil compensation
- **Right Click**: Show detailed status
- **Middle Click**: Cycle weapon categories
- **ESC**: Exit script

### 🎨 **Weapon Categories**
- **All**: All available weapons
- **Rifle**: Assault rifles and battle rifles
- **SMG**: Submachine guns
- **Sniper**: Sniper rifles
- **LMG**: Light machine guns
- **Generic**: Default patterns

### ⚡ **Performance Features**
- **Logitech Mode**: Optimized movement for Logitech mice
- **Randomization**: Adds slight variation to prevent detection
- **Auto Detection**: Automatically switches based on active game
- **Smooth Movement**: Gradual mouse movements for better accuracy

## Installation

1. **Download Files**:
   - `enhanced_no_recoil.ps1` - Main script
   - `weapon_config.json` - Weapon configuration
   - `run_enhanced_script.bat` - Easy launcher

2. **Run as Administrator**:
   - Right-click `run_enhanced_script.bat`
   - Select "Run as administrator"

3. **Alternative Method**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "enhanced_no_recoil.ps1"
   ```

## Configuration

### Adding New Weapons

Edit `weapon_config.json` to add new weapons:

```json
{
  "weapons": {
    "game_name": {
      "weapon_name": {
        "pattern": [[0,2], [1,2], [-1,2], [0,2], [1,2]],
        "delay": 80,
        "description": "Weapon description",
        "category": "Rifle",
        "recoil_level": "Medium"
      }
    }
  }
}
```

### Pattern Format
- `pattern`: Array of [x, y] coordinates for mouse movement
- `delay`: Milliseconds between movements
- `description`: Human-readable weapon description
- `category`: Weapon category (Rifle, SMG, Sniper, LMG, Generic)
- `recoil_level`: Low, Medium, or High

### Settings
```json
{
  "settings": {
    "default_sensitivity": 1.0,
    "default_delay": 100,
    "logitech_mode": true,
    "auto_detect": true
  }
}
```

## Usage

1. **Start the Script**: Run `run_enhanced_script.bat` as administrator
2. **Select Weapon**: Press F2 to cycle through weapons
3. **Adjust Sensitivity**: Press F3 to adjust sensitivity
4. **Enable Script**: Press F1 to activate
5. **Use in Game**: Hold left mouse button while firing

## Status Display

Press **Right Click** to see detailed status:
- Script status (ON/OFF)
- Detected game
- Current weapon and category
- Sensitivity setting
- Feature toggles

## Troubleshooting

### Script Not Working
1. **Run as Administrator**: Required for mouse control
2. **Check Execution Policy**: Use the batch file or bypass policy
3. **Verify Game Detection**: Check if your game is supported

### Weapon Patterns Not Loading
1. **Check JSON File**: Ensure `weapon_config.json` is in the same folder
2. **Validate JSON**: Use online JSON validator
3. **Fallback**: Script uses built-in patterns if JSON fails

### Performance Issues
1. **Disable Logitech Mode**: Press F4 to toggle
2. **Reduce Sensitivity**: Press F3 to lower sensitivity
3. **Close Other Scripts**: Ensure no conflicting scripts are running

## Safety Features

- **Randomization**: Adds variation to prevent detection
- **Smooth Movement**: Gradual mouse movements
- **Configurable Sensitivity**: Adjust for different games
- **Auto Detection**: Automatically adapts to different games

## Supported Games

| Game | Detection | Weapons |
|------|-----------|---------|
| CS:GO | ✅ | AK-47, M4A1, AWP, M4A4, FAMAS, Galil |
| Valorant | ✅ | Vandal, Phantom, Spectre, Operator, Guardian |
| PUBG | ✅ | AKM, M416, SCAR-L, UMP45, M249, DP28 |
| Apex | ✅ | R-301, Flatline, Spitfire |
| Fortnite | ✅ | Generic patterns |
| Overwatch | ✅ | Generic patterns |
| COD/Warzone | ✅ | Generic patterns |
| Rainbow Six | ✅ | Generic patterns |

## File Structure

```
script/
├── enhanced_no_recoil.ps1      # Main enhanced script
├── weapon_config.json          # Weapon configuration
├── run_enhanced_script.bat     # Easy launcher
├── ENHANCED_README.md         # This documentation
├── universal_no_recoil.ps1     # Original script
└── weapon_config.json          # Configuration file
```

## Changelog

### Enhanced Version Features
- ✅ JSON configuration system
- ✅ Advanced game detection
- ✅ Weapon categorization
- ✅ Randomization feature
- ✅ Enhanced status display
- ✅ Improved mouse movement
- ✅ More weapon patterns
- ✅ Better error handling

## Disclaimer

This script is for educational purposes only. Use at your own risk and in accordance with game terms of service. 