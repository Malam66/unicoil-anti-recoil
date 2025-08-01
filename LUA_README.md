# Lua No Recoil Scripts

This directory contains Lua scripts for no-recoil functionality, similar to the script shown in the image.

## Files

### 1. `simple_no_recoil.lua`
**Basic version** - Exactly like the script in the image:
- Moves mouse down by 5 pixels when both middle mouse button (button 3) and left mouse button (button 1) are held
- Simple and straightforward
- No configuration needed

### 2. `enhanced_no_recoil.lua`
**Advanced version** with additional features:
- Multiple recoil patterns (default, strong, weak, ak47, m4a1, sniper)
- Adjustable sensitivity
- Toggle functionality
- Pattern switching

## How to Use

### For Logitech Gaming Software (LGS) / G HUB:
1. Open Logitech Gaming Software or G HUB
2. Select your mouse
3. Go to "Scripting" or "Lua Scripts"
4. Copy and paste the desired script
5. Save and activate the script

### Controls for Enhanced Script:
- **Scroll Lock**: Toggle script on/off
- **Mouse Button 5 (Side Button)**: Change recoil pattern
- **Mouse Button 4 (Side Button)**: Adjust sensitivity
- **Middle Mouse + Left Click**: Trigger recoil compensation

### Recoil Patterns Available:
- **default**: Basic downward movement (5 pixels)
- **strong**: Stronger recoil with horizontal variation
- **weak**: Lighter recoil (3 pixels)
- **ak47**: AK-47 style pattern with horizontal sway
- **m4a1**: M4A1 style pattern
- **sniper**: High vertical recoil for sniper rifles

## Features

### Simple Script:
- ✅ Basic recoil compensation
- ✅ Easy to understand
- ✅ No configuration needed
- ✅ Works with any Logitech mouse

### Enhanced Script:
- ✅ Multiple weapon patterns
- ✅ Adjustable sensitivity (0.5 - 2.0)
- ✅ Toggle on/off functionality
- ✅ Pattern switching
- ✅ Real-time feedback via Logitech software
- ✅ Customizable delay settings

## Compatibility

These scripts work with:
- Logitech Gaming Software (LGS)
- Logitech G HUB
- Any Logitech gaming mouse
- Most FPS games (CS:GO, Valorant, PUBG, etc.)

## Safety Notes

⚠️ **Important**: 
- These scripts are for educational purposes
- Use at your own risk
- Some games may detect and ban for using macros
- Always check your game's terms of service
- Test in practice mode before using in competitive matches

## Customization

You can modify the `enhanced_no_recoil.lua` script to:
- Add new recoil patterns
- Change sensitivity ranges
- Modify delay times
- Add new control schemes
- Customize for specific weapons

## Troubleshooting

1. **Script not working**: Make sure Logitech software is running and script is activated
2. **Mouse buttons not responding**: Check if your mouse has the required buttons (3, 4, 5)
3. **Pattern not changing**: Verify mouse button 5 is properly configured
4. **Sensitivity not adjusting**: Check mouse button 4 configuration

## Comparison with PowerShell Scripts

The Lua scripts are simpler but more compatible with Logitech hardware, while the PowerShell scripts offer:
- More advanced features
- JSON configuration
- Game detection
- Cross-platform compatibility
- More customization options

Choose based on your needs and hardware setup. 