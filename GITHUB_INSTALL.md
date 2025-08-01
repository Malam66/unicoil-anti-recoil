# 🚀 GitHub Installation Guide for UniCoil

This guide will show you how to install UniCoil from GitHub using different methods.

## 📋 Prerequisites

Before installing, make sure you have:
- **Python 3.8 or higher** installed
- **Git** installed (for cloning)
- **Windows 10/11** (the system is designed for Windows)
- **Administrator privileges** (for mouse control features)

## 🔧 Installation Methods

### Method 1: Git Clone (Recommended for Developers)

#### Step 1: Clone the Repository
```bash
# Open Command Prompt or PowerShell
# Navigate to your desired directory
cd C:\Users\YourUsername\Desktop

# Clone the repository
git clone https://github.com/yourusername/unicoil-anti-recoil.git

# Navigate into the project directory
cd unicoil-anti-recoil
```

#### Step 2: Install Dependencies
```bash
# Install all required Python packages
pip install -r requirements.txt
```

#### Step 3: Run the Application
```bash
# Run the universal version (recommended)
python universal_antirecoil_app.py

# Or run the launcher to choose your version
python launcher.py

# Or use the batch file (Windows)
run_antirecoil_app.bat
```

### Method 2: Direct Download (For Users)

#### Step 1: Download from GitHub
1. Go to the GitHub repository: `https://github.com/yourusername/unicoil-anti-recoil`
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract the ZIP file to your desired location

#### Step 2: Open Command Prompt
```bash
# Navigate to the extracted folder
cd C:\Users\YourUsername\Downloads\unicoil-anti-recoil-master
```

#### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

#### Step 4: Run the Application
```bash
# Run the universal version
python universal_antirecoil_app.py
```

### Method 3: Using pip (Advanced Users)

#### Step 1: Install via pip
```bash
# Install directly from GitHub
pip install git+https://github.com/yourusername/unicoil-anti-recoil.git

# Or install in development mode
pip install -e git+https://github.com/yourusername/unicoil-anti-recoil.git#egg=unicoil-anti-recoil
```

#### Step 2: Run the Application
```bash
# Use the command-line interface
unicoil

# Or run the launcher
unicoil-launcher
```

## 🎮 Quick Start Guide

### First Time Setup

1. **Launch the Application**
   ```bash
   python universal_antirecoil_app.py
   ```

2. **Configure Game Detection**
   - Enable "Auto-Detect Game"
   - Or manually select your game from the dropdown

3. **Adjust Settings**
   - Set recoil mode (LOW, MEDIUM, HIGH, CUSTOM)
   - Adjust sensitivity multiplier
   - Configure vertical/horizontal recoil

4. **Enable Recoil Control**
   - Check "Enable Recoil Control"
   - The status should show "ON"

5. **Test in Game**
   - Start your game
   - The app should automatically detect it
   - Test the recoil control

### Configuration Files

The application uses several configuration files:

- **`universal_games.json`**: Game-specific settings and weapon profiles
- **`pubg_weapons.json`**: Weapon recoil patterns
- **`config_slot_*.json`**: User configuration slots

## 🔧 Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError: No module named 'psutil'
```bash
# Solution: Install the missing module
pip install psutil==5.9.5
```

#### 2. Permission Denied
- **Solution**: Run Command Prompt as Administrator
- Right-click Command Prompt → "Run as administrator"

#### 3. Game Not Detected
- **Solution**: Check if the game is running
- Verify the process name in `universal_games.json`
- Try manual game selection

#### 4. Recoil Not Working
- **Solution**: 
  - Ensure recoil control is enabled
  - Check sensitivity settings
  - Verify the game window is in focus
  - Try different recoil modes

### Debug Mode

Run with debug output to troubleshoot:
```bash
python universal_antirecoil_app.py --debug
```

## 📁 Project Structure

After installation, your directory should look like this:
```
unicoil-anti-recoil/
├── universal_antirecoil_app.py    # 🌟 Universal version
├── anti_recoil_app.py             # Basic version
├── enhanced_antirecoil_app.py     # Enhanced version
├── launcher.py                    # Application launcher
├── universal_games.json           # Game configurations
├── pubg_weapons.json              # Weapon profiles
├── requirements.txt               # Python dependencies
├── run_antirecoil_app.bat        # Windows launcher
├── test_deployment.py            # Deployment tests
├── deploy.py                     # Auto-deployment script
├── setup.py                      # Installation script
├── README.md                     # Main documentation
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore file
└── .github/                      # GitHub Actions
    └── workflows/
        └── test.yml              # Automated testing
```

## 🔄 Updating

### Update from GitHub
```bash
# Navigate to the project directory
cd unicoil-anti-recoil

# Pull latest changes
git pull origin main

# Reinstall dependencies
pip install -r requirements.txt
```

### Check for Updates
```bash
# Check current version
python -c "import universal_antirecoil_app; print('Version:', universal_antirecoil_app.__version__)"
```

## 🛡️ Security Notes

- **Administrator Rights**: The application needs administrator privileges for mouse control
- **Antivirus**: Some antivirus software may flag the application - add it to exclusions
- **Game Terms**: Ensure compliance with your game's terms of service

## 📞 Support

If you encounter issues:

1. **Check the Troubleshooting section above**
2. **Search existing issues**: [GitHub Issues](https://github.com/yourusername/unicoil-anti-recoil/issues)
3. **Create a new issue**: Include your system info and error messages
4. **Join discussions**: [GitHub Discussions](https://github.com/yourusername/unicoil-anti-recoil/discussions)

## 🎯 Next Steps

After successful installation:

1. **Read the main README.md** for detailed usage instructions
2. **Configure your game settings** in the application
3. **Test with your favorite games**
4. **Join the community** for tips and updates

---

**🎮 Happy Gaming with UniCoil!**

For more information, visit: [GitHub Repository](https://github.com/yourusername/unicoil-anti-recoil) 