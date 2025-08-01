# 🎯 UniCoil - Universal Anti-Recoil Control System

A powerful, universal anti-recoil control system that automatically detects and adapts to 20+ popular shooting games.

![UniCoil Logo](https://img.shields.io/badge/UniCoil-Universal%20Anti--Recoil-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

## 🌟 Features

### 🎮 **Universal Game Support**
- **Automatic Game Detection** - Detects 20+ popular games
- **Game-Specific Settings** - Optimized recoil patterns for each game
- **Real-Time Adaptation** - Adjusts settings automatically
- **Cross-Platform Compatibility** - Works with any shooting game

### 🎯 **Supported Games**
- **CS:GO / Counter-Strike 2**
- **Valorant**
- **PUBG**
- **Apex Legends**
- **Fortnite**
- **Overwatch**
- **Call of Duty / Warzone**
- **Rainbow Six Siege**
- **Battlefield**
- **Destiny 2**
- **Halo**
- **Team Fortress 2**
- **Left 4 Dead 2**
- **GTA V**
- **Red Dead Redemption 2**
- **Cyberpunk 2077**
- **The Division 2**
- **Escape from Tarkov**

### 🛠️ **Advanced Features**
- **Three Application Versions**: Basic, Enhanced, and Universal
- **Lua Script Integration**: Support for existing Lua scripts
- **Weapon-Specific Profiles**: Custom recoil patterns for different weapons
- **Sensitivity Control**: Adjustable sensitivity multiplier
- **Real-Time Monitoring**: Live game detection and status updates
- **Configuration Management**: Save/load settings for different games

## 🚀 Quick Start

### Prerequisites
- **Python 3.8 or higher**
- **Windows 10/11**
- **Administrator privileges** (for mouse control)

### Installation

#### Method 1: GitHub Clone (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/unicoil-anti-recoil.git

# Navigate to the directory
cd unicoil-anti-recoil

# Install dependencies
pip install -r requirements.txt

# Run the universal app
python universal_antirecoil_app.py
```

#### Method 2: Direct Download
```bash
# Download and extract the ZIP file
# Navigate to the extracted directory
cd unicoil-anti-recoil

# Install dependencies
pip install -r requirements.txt

# Run the application
python launcher.py
```

#### Method 3: Batch File (Windows)
```bash
# Double-click the batch file
run_antirecoil_app.bat
```

## 📁 Project Structure

```
unicoil-anti-recoil/
├── universal_antirecoil_app.py    # 🌟 Universal version (Recommended)
├── anti_recoil_app.py             # Basic version
├── enhanced_antirecoil_app.py     # Enhanced version
├── launcher.py                    # Application launcher
├── universal_games.json           # Game configurations
├── pubg_weapons.json              # Weapon profiles
├── requirements.txt               # Python dependencies
├── run_antirecoil_app.bat        # Windows launcher
├── test_deployment.py            # Deployment tests
├── deploy.py                     # Auto-deployment script
├── enhanced_no_recoil.lua        # Lua script integration
├── simple_no_recoil.lua          # Simple Lua script
└── README.md                     # This file
```

## 🎮 Usage Guide

### Launching the Application

1. **Universal Version (Recommended)**
   ```bash
   python universal_antirecoil_app.py
   ```
   - Automatically detects games
   - Game-specific settings
   - Real-time adaptation

2. **Launcher (Choose Version)**
   ```bash
   python launcher.py
   ```
   - Choose between Basic, Enhanced, or Universal
   - Easy version selection

3. **Batch File (Windows)**
   ```bash
   run_antirecoil_app.bat
   ```
   - One-click launch
   - Automatic dependency installation

### Configuration

#### Game Detection
- **Auto-Detect**: Automatically detects running games
- **Manual Selection**: Choose specific games manually
- **Real-Time Updates**: Status updates every 5 seconds

#### Recoil Control
- **Enable/Disable**: Toggle recoil control on/off
- **Mode Selection**: LOW, MEDIUM, HIGH, CUSTOM
- **Sensitivity**: Adjust sensitivity multiplier (0.1-3.0)
- **Vertical/Horizontal**: Separate control for recoil direction

#### Weapon Selection
- **Game-Specific Weapons**: Different weapons for each game
- **Weapon Information**: Description, category, recoil level
- **Custom Patterns**: User-defined recoil patterns

#### Advanced Settings
- **Lua Integration**: Use existing Lua scripts
- **ADS Requirement**: Require aim down sights
- **Configuration Slots**: Save/load different settings

## 🔧 Configuration Files

### Game Configuration (`universal_games.json`)
```json
{
  "games": {
    "CS:GO": {
      "processes": ["csgo.exe", "cs2.exe"],
      "weapons": {
        "ak47": {
          "pattern": [[0,6], [2,6], [-2,6], [0,6], [2,6]],
          "delay": 100,
          "description": "AK-47 - High recoil",
          "category": "Rifle",
          "recoil_level": "High"
        }
      },
      "default_sensitivity": 1.0,
      "default_mode": "MEDIUM"
    }
  }
}
```

### Weapon Configuration (`pubg_weapons.json`)
```json
{
  "m416": {
    "pattern": [[0,3], [1,3], [-1,3], [0,3], [1,3]],
    "delay": 75,
    "description": "M416 - Most stable AR",
    "category": "Assault Rifle",
    "recoil_level": "Low"
  }
}
```

## 🛡️ Safety Features

- **Game Detection**: Only works when games are detected
- **Configurable Sensitivity**: Adjustable for different games
- **ADS Requirement**: Optional aim down sights requirement
- **Lua Integration**: Support for existing scripts
- **Error Handling**: Graceful error handling and recovery

## ⚠️ Legal Disclaimer

This software is provided for educational and personal use only. Users are responsible for complying with the terms of service of the games they play. The developers are not responsible for any consequences resulting from the use of this software.

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'psutil'**
   ```bash
   pip install psutil==5.9.5
   ```

2. **Permission Denied**
   - Run as Administrator
   - Check Windows Defender settings

3. **Game Not Detected**
   - Ensure game is running
   - Check process names in `universal_games.json`
   - Try manual game selection

4. **Recoil Not Working**
   - Check if recoil control is enabled
   - Adjust sensitivity settings
   - Verify game is in focus

### Debug Mode
```bash
# Run with debug output
python universal_antirecoil_app.py --debug
```

## 🔄 Updates

### Version History
- **v1.0.0**: Initial release with basic functionality
- **v1.1.0**: Added enhanced version with advanced features
- **v1.2.0**: Universal version with game detection
- **v1.3.0**: Added 20+ game support and real-time adaptation

### Updating
```bash
# Pull latest changes
git pull origin main

# Reinstall dependencies
pip install -r requirements.txt
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/unicoil-anti-recoil/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/unicoil-anti-recoil/discussions)
- **Wiki**: [Documentation](https://github.com/yourusername/unicoil-anti-recoil/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Lua Script Community**: For existing anti-recoil scripts
- **Python Community**: For excellent libraries and tools
- **Gaming Community**: For feedback and testing

---

**⭐ Star this repository if you find it helpful!**

**🎮 Happy Gaming!** 