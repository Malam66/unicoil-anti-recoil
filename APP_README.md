# UniCoil - Anti Recoil Control Application

A modern GUI application for controlling recoil in shooting games, featuring a dark theme and advanced functionality similar to professional anti-recoil tools.

## Features

### 🎯 **Core Functionality**
- **Anti-Recoil Control**: Compensate for weapon recoil in real-time
- **Rapid Fire**: Adjustable rapid fire functionality
- **Weapon Profiles**: Pre-configured weapon patterns from JSON files
- **Real-time Monitoring**: Continuous mouse input monitoring
- **Configurable Settings**: Adjustable strength, delay, and speed parameters

### 🎮 **Game Integration**
- **Multiple Game Support**: Works with popular shooting games
- **Auto-Detection**: Automatically detects active games
- **Lua Script Integration**: Compatible with existing Lua scripts
- **Weapon-Specific Patterns**: Different recoil patterns for different weapons

### 🎨 **User Interface**
- **Dark Theme**: Professional dark interface with gold accents
- **Real-time Status**: Live status indicators for all features
- **Configuration Slots**: Save and load multiple configurations
- **Weapon Selection**: Dropdown menu for weapon selection
- **Advanced Controls**: Additional options for power users

## Installation

### Prerequisites
- Python 3.7 or higher
- Windows 10/11 (for mouse control functionality)

### Quick Start
1. **Download Files**: Ensure all files are in the same directory
2. **Run Installer**: Double-click `run_antirecoil_app.bat`
3. **Launch Application**: The app will start automatically

### Manual Installation
```bash
# Install required packages
pip install -r requirements.txt

# Run the application
python anti_recoil_app.py
# or
python enhanced_antirecoil_app.py
```

## Usage

### Basic Operation
1. **Launch the Application**: Run the batch file or Python script
2. **Enable Recoil Control**: Check the "Enable" checkbox
3. **Adjust Settings**: Use sliders to configure recoil parameters
4. **Select Weapon**: Choose from available weapon profiles
5. **Test in Game**: The application will automatically monitor mouse input

### Configuration Options

#### Anti-Recoil Settings
- **Strength**: Controls the intensity of recoil compensation (0-10)
- **Delay**: Time between recoil compensation movements (0-200ms)
- **Mode**: Pre-configured modes (LOW, MEDIUM, HIGH, CUSTOM)
- **ADS Requirement**: Option to only activate when aiming down sights

#### Rapid Fire Settings
- **Speed**: Controls rapid fire rate (0-20 clicks per second)
- **ADS Requirement**: Option to only activate when aiming down sights

#### Advanced Options
- **Lua Script Integration**: Use existing Lua scripts for enhanced functionality
- **Auto-Detect Game**: Automatically detect and adapt to different games
- **Theme Toggle**: Switch between dark and light themes
- **Caps Lock Toggle**: Use caps lock key for additional control

### Weapon Profiles

The application supports weapon-specific recoil patterns loaded from JSON files:

```json
{
  "weapon_name": {
    "pattern": [[0,2], [1,2], [-1,2], [0,2], [1,2]],
    "delay": 80,
    "description": "Weapon description",
    "category": "Assault Rifle",
    "recoil_level": "Medium"
  }
}
```

### Configuration Slots

Save and load different configurations:
1. **Select Slot**: Choose configuration slot (1-10)
2. **Adjust Settings**: Modify recoil parameters
3. **Save Config**: Click "SAVE CONFIG" to store settings
4. **Load Config**: Click "LOAD CONFIG" to restore settings

## File Structure

```
script/
├── anti_recoil_app.py              # Basic anti-recoil application
├── enhanced_antirecoil_app.py      # Enhanced version with more features
├── requirements.txt                 # Python dependencies
├── run_antirecoil_app.bat          # Easy launcher for Windows
├── pubg_weapons.json               # Weapon configuration file
├── enhanced_no_recoil.lua          # Lua script for advanced functionality
├── simple_no_recoil.lua            # Simple Lua script
├── APP_README.md                   # This documentation
├── ENHANCED_README.md              # Lua script documentation
└── LUA_README.md                   # Basic Lua script documentation
```

## Supported Games

| Game | Detection | Weapons | Status |
|------|-----------|---------|--------|
| CS:GO | ✅ | AK-47, M4A1, AWP, M4A4, FAMAS, Galil | Full Support |
| Valorant | ✅ | Vandal, Phantom, Spectre, Operator, Guardian | Full Support |
| PUBG | ✅ | AKM, M416, SCAR-L, UMP45, M249, DP28 | Full Support |
| Apex Legends | ✅ | R-301, Flatline, Spitfire | Full Support |
| Fortnite | ✅ | Generic patterns | Basic Support |
| Overwatch | ✅ | Generic patterns | Basic Support |
| Call of Duty | ✅ | Generic patterns | Basic Support |
| Rainbow Six Siege | ✅ | Generic patterns | Basic Support |

## Troubleshooting

### Common Issues

#### Application Won't Start
1. **Check Python Installation**: Ensure Python 3.7+ is installed
2. **Install Dependencies**: Run `pip install -r requirements.txt`
3. **Run as Administrator**: Right-click and "Run as administrator"

#### Recoil Control Not Working
1. **Enable Feature**: Ensure recoil control is enabled in the app
2. **Check Game**: Make sure the game is running and active
3. **Adjust Settings**: Try different strength and delay values
4. **Run as Administrator**: Required for mouse control

#### Lua Integration Issues
1. **Check File**: Ensure `enhanced_no_recoil.lua` exists
2. **Logitech Software**: Lua scripts require Logitech Gaming Software
3. **Permissions**: Run as administrator for full functionality

### Performance Optimization
1. **Reduce Monitoring Frequency**: Lower the monitoring delay
2. **Disable Unused Features**: Turn off features you don't need
3. **Close Other Applications**: Free up system resources
4. **Update Drivers**: Ensure mouse drivers are up to date

## Safety Features

- **Configurable Sensitivity**: Adjust for different games and weapons
- **Smooth Movement**: Gradual mouse movements for better accuracy
- **Randomization**: Adds variation to prevent detection
- **Auto-Detection**: Automatically adapts to different games
- **Error Handling**: Graceful error handling and recovery

## Legal Disclaimer

This application is provided for educational and research purposes only. Users are responsible for:
- Complying with game terms of service
- Using the application responsibly
- Understanding local laws and regulations
- Not using in competitive or ranked matches where prohibited

The developers are not responsible for any consequences resulting from the use of this software.

## Technical Details

### Dependencies
- `tkinter`: GUI framework (included with Python)
- `keyboard`: Keyboard input monitoring
- `mouse`: Mouse input monitoring and control
- `Pillow`: Image processing (for future features)
- `json`: Configuration file handling
- `threading`: Multi-threading for monitoring
- `time`: Timing and delays

### Architecture
- **GUI Layer**: Tkinter-based user interface
- **Control Layer**: Configuration and settings management
- **Monitoring Layer**: Real-time input monitoring
- **Integration Layer**: Lua script and game integration
- **Configuration Layer**: JSON-based weapon profiles

### Performance
- **Low CPU Usage**: Efficient monitoring with minimal resource consumption
- **Real-time Response**: Immediate reaction to mouse input
- **Configurable Delays**: Adjustable timing for different scenarios
- **Memory Efficient**: Minimal memory footprint

## Development

### Adding New Features
1. **Modify GUI**: Add new widgets in the appropriate section
2. **Update Monitoring**: Add new monitoring logic in `monitor_input()`
3. **Configuration**: Add new settings to configuration system
4. **Documentation**: Update this README with new features

### Adding New Weapons
1. **Edit JSON**: Add weapon data to `pubg_weapons.json`
2. **Test Pattern**: Verify recoil pattern works correctly
3. **Update GUI**: Add weapon to dropdown if needed
4. **Document**: Add weapon to supported weapons list

### Contributing
1. **Fork Repository**: Create your own fork
2. **Make Changes**: Implement new features or fixes
3. **Test Thoroughly**: Ensure all functionality works
4. **Submit Pull Request**: Submit changes for review

## Version History

### v2.0 (Enhanced Version)
- ✅ Advanced GUI with dark theme
- ✅ Weapon profile integration
- ✅ Configuration slot system
- ✅ Lua script integration
- ✅ Real-time status monitoring
- ✅ Multiple game support

### v1.0 (Basic Version)
- ✅ Basic anti-recoil functionality
- ✅ Simple GUI interface
- ✅ Configurable settings
- ✅ Mouse input monitoring

## Support

For issues, questions, or feature requests:
1. **Check Documentation**: Review this README and other documentation
2. **Test Configuration**: Try different settings and configurations
3. **Check Compatibility**: Ensure your system meets requirements
4. **Report Issues**: Document the problem with detailed information

## License

This project is provided as-is for educational purposes. Use at your own risk and in accordance with applicable laws and game terms of service. 