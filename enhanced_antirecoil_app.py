import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import threading
import time
import keyboard
import mouse
import subprocess
import os
import sys
from PIL import Image, ImageTk

class EnhancedAntiRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("R6 No Recoil - Enhanced Control")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Dark theme colors
        self.bg_color = "#0a0a0a"
        self.fg_color = "#ffffff"
        self.accent_color = "#ffd700"  # Gold
        self.button_color = "#333333"
        self.button_hover = "#444444"
        self.success_color = "#00ff00"
        self.warning_color = "#ffff00"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.recoil_enabled = False
        self.current_mode = "MEDIUM"
        self.caps_lock_toggle = False
        self.vertical_recoil = tk.IntVar(value=3)
        self.horizontal_recoil = tk.IntVar(value=0)
        self.weapons = self.load_weapons()
        self.current_weapon = "default"
        self.lua_process = None
        
        # Create GUI
        self.create_widgets()
        
        # Start monitoring thread
        self.monitoring = False
        self.start_monitoring()
        
    def load_weapons(self):
        """Load weapon configurations from JSON file"""
        try:
            with open('pubg_weapons.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default weapons if file not found
            return {
                "default": {
                    "pattern": [[0,2], [0,2], [0,2], [0,2], [0,2]],
                    "delay": 80,
                    "description": "Default pattern",
                    "category": "Generic",
                    "recoil_level": "Medium"
                }
            }
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title
        title_label = tk.Label(
            self.root,
            text="R6 No Recoil",
            font=("Arial", 28, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # Recoil Control Section
        self.create_recoil_control_section()
        
        # Current Recoil Settings Section
        self.create_recoil_settings_section()
        
        # Weapon Selection Section
        self.create_weapon_section()
        
        # Advanced Controls Section
        self.create_advanced_section()
        
        # Bottom Buttons
        self.create_bottom_buttons()
        
    def create_recoil_control_section(self):
        """Create recoil control section"""
        control_frame = tk.LabelFrame(
            self.root,
            text="Recoil Control",
            font=("Arial", 14, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        control_frame.pack(fill="x", padx=20, pady=10)
        
        # Enable status
        self.enable_var = tk.BooleanVar()
        enable_check = tk.Checkbutton(
            control_frame,
            text="Enable:",
            font=("Arial", 12, "bold"),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.enable_var,
            command=self.toggle_recoil
        )
        enable_check.pack(anchor="w", padx=10, pady=5)
        
        # Status label
        self.status_label = tk.Label(
            control_frame,
            text="OFF",
            font=("Arial", 12, "bold"),
            fg=self.warning_color,
            bg=self.bg_color
        )
        self.status_label.pack(anchor="w", padx=30, pady=2)
        
        # Mode selection
        mode_frame = tk.Frame(control_frame, bg=self.bg_color)
        mode_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            mode_frame,
            text="Mode:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.mode_var = tk.StringVar(value="MEDIUM")
        mode_combo = ttk.Combobox(
            mode_frame,
            textvariable=self.mode_var,
            values=["LOW", "MEDIUM", "HIGH", "CUSTOM"],
            state="readonly",
            font=("Arial", 10),
            width=10
        )
        mode_combo.pack(side="left", padx=10)
        mode_combo.bind("<<ComboboxSelected>>", self.change_mode)
        
        # Mode description
        self.mode_desc_label = tk.Label(
            control_frame,
            text="MEDIUM: Ideal for Medium Recoil Assault Rifles",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.mode_desc_label.pack(anchor="w", padx=10, pady=2)
        
        # Caps Lock Toggle
        caps_frame = tk.Frame(control_frame, bg=self.bg_color)
        caps_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            caps_frame,
            text="Caps Lock Toggle:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.caps_var = tk.BooleanVar()
        caps_check = tk.Checkbutton(
            caps_frame,
            text="",
            variable=self.caps_var,
            command=self.toggle_caps_lock
        )
        caps_check.pack(side="left", padx=10)
        
    def create_recoil_settings_section(self):
        """Create current recoil settings section"""
        settings_frame = tk.LabelFrame(
            self.root,
            text="Current Recoil Settings",
            font=("Arial", 14, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        # Vertical recoil
        vert_frame = tk.Frame(settings_frame, bg=self.bg_color)
        vert_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            vert_frame,
            text="Vertical:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        vert_slider = tk.Scale(
            vert_frame,
            from_=0,
            to=10,
            orient="horizontal",
            variable=self.vertical_recoil,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        vert_slider.pack(side="right", fill="x", expand=True, padx=10)
        
        # Horizontal recoil
        horiz_frame = tk.Frame(settings_frame, bg=self.bg_color)
        horiz_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            horiz_frame,
            text="Horizontal:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        horiz_slider = tk.Scale(
            horiz_frame,
            from_=0,
            to=10,
            orient="horizontal",
            variable=self.horizontal_recoil,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        horiz_slider.pack(side="right", fill="x", expand=True, padx=10)
        
    def create_weapon_section(self):
        """Create weapon selection section"""
        weapon_frame = tk.LabelFrame(
            self.root,
            text="Weapon Selection",
            font=("Arial", 14, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        weapon_frame.pack(fill="x", padx=20, pady=10)
        
        # Weapon dropdown
        weapon_select_frame = tk.Frame(weapon_frame, bg=self.bg_color)
        weapon_select_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            weapon_select_frame,
            text="Weapon:",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        weapon_names = list(self.weapons.keys())
        self.weapon_var = tk.StringVar(value=weapon_names[0])
        weapon_combo = ttk.Combobox(
            weapon_select_frame,
            textvariable=self.weapon_var,
            values=weapon_names,
            state="readonly",
            font=("Arial", 10),
            width=20
        )
        weapon_combo.pack(side="right", padx=10)
        weapon_combo.bind("<<ComboboxSelected>>", self.change_weapon)
        
        # Weapon info
        self.weapon_info_label = tk.Label(
            weapon_frame,
            text="",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            wraplength=400
        )
        self.weapon_info_label.pack(anchor="w", padx=10, pady=5)
        
        # Update weapon info
        self.update_weapon_info()
        
    def create_advanced_section(self):
        """Create advanced controls section"""
        advanced_frame = tk.LabelFrame(
            self.root,
            text="Advanced Controls",
            font=("Arial", 14, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        advanced_frame.pack(fill="x", padx=20, pady=10)
        
        # Lua script integration
        lua_frame = tk.Frame(advanced_frame, bg=self.bg_color)
        lua_frame.pack(fill="x", padx=10, pady=5)
        
        self.lua_var = tk.BooleanVar()
        lua_check = tk.Checkbutton(
            lua_frame,
            text="Use Lua Script Integration",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.lua_var,
            command=self.toggle_lua_integration
        )
        lua_check.pack(side="left")
        
        # Auto-detect game
        game_frame = tk.Frame(advanced_frame, bg=self.bg_color)
        game_frame.pack(fill="x", padx=10, pady=5)
        
        self.game_var = tk.BooleanVar(value=True)
        game_check = tk.Checkbutton(
            game_frame,
            text="Auto-detect Game",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.game_var
        )
        game_check.pack(side="left")
        
    def create_bottom_buttons(self):
        """Create bottom buttons"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        
        # Create buttons in a grid
        buttons = [
            ("Toggle Recoil", self.toggle_recoil),
            ("Change Mode", self.change_mode),
            ("Toggle Theme", self.toggle_theme),
            ("Caps Lock Toggle", self.toggle_caps_lock)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 10, "bold"),
                bg=self.button_color,
                fg=self.fg_color,
                relief="flat",
                command=command
            )
            btn.grid(row=0, column=i, padx=5, pady=5, sticky="ew")
            button_frame.columnconfigure(i, weight=1)
        
    def toggle_recoil(self):
        """Toggle recoil control"""
        self.recoil_enabled = self.enable_var.get()
        if self.recoil_enabled:
            self.status_label.config(text="ON", fg=self.success_color)
            print("Recoil Control: ENABLED")
        else:
            self.status_label.config(text="OFF", fg=self.warning_color)
            print("Recoil Control: DISABLED")
            
    def change_mode(self, event=None):
        """Change recoil mode"""
        self.current_mode = self.mode_var.get()
        mode_descriptions = {
            "LOW": "LOW: Ideal for Low Recoil Weapons",
            "MEDIUM": "MEDIUM: Ideal for Medium Recoil Assault Rifles",
            "HIGH": "HIGH: Ideal for High Recoil Weapons",
            "CUSTOM": "CUSTOM: User-defined recoil pattern"
        }
        self.mode_desc_label.config(text=mode_descriptions.get(self.current_mode, ""))
        print(f"Mode changed to: {self.current_mode}")
        
    def toggle_theme(self):
        """Toggle between light and dark theme"""
        if self.bg_color == "#0a0a0a":  # Dark theme
            self.bg_color = "#f0f0f0"
            self.fg_color = "#000000"
            self.button_color = "#cccccc"
        else:  # Light theme
            self.bg_color = "#0a0a0a"
            self.fg_color = "#ffffff"
            self.button_color = "#333333"
            
        self.root.configure(bg=self.bg_color)
        # Update all widgets (simplified for demo)
        print("Theme toggled")
        
    def toggle_caps_lock(self):
        """Toggle caps lock functionality"""
        self.caps_lock_toggle = self.caps_var.get()
        status = "ENABLED" if self.caps_lock_toggle else "DISABLED"
        print(f"Caps Lock Toggle: {status}")
        
    def change_weapon(self, event=None):
        """Change selected weapon"""
        self.current_weapon = self.weapon_var.get()
        self.update_weapon_info()
        print(f"Weapon changed to: {self.current_weapon}")
        
    def update_weapon_info(self):
        """Update weapon information display"""
        if self.current_weapon in self.weapons:
            weapon = self.weapons[self.current_weapon]
            info_text = f"{weapon.get('description', 'No description')}\n"
            info_text += f"Category: {weapon.get('category', 'Unknown')}\n"
            info_text += f"Recoil Level: {weapon.get('recoil_level', 'Unknown')}\n"
            info_text += f"Delay: {weapon.get('delay', 0)}ms"
            self.weapon_info_label.config(text=info_text)
            
    def toggle_lua_integration(self):
        """Toggle Lua script integration"""
        if self.lua_var.get():
            # Start Lua script
            try:
                if os.path.exists("enhanced_no_recoil.lua"):
                    # For demonstration, we'll just print that Lua integration is enabled
                    print("Lua Script Integration: ENABLED")
                    messagebox.showinfo("Lua Integration", "Lua script integration enabled")
                else:
                    messagebox.showwarning("Lua Script", "enhanced_no_recoil.lua not found")
                    self.lua_var.set(False)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to start Lua script: {str(e)}")
                self.lua_var.set(False)
        else:
            print("Lua Script Integration: DISABLED")
            
    def start_monitoring(self):
        """Start the monitoring thread for recoil control"""
        self.monitoring = True
        monitor_thread = threading.Thread(target=self.monitor_input, daemon=True)
        monitor_thread.start()
        
    def monitor_input(self):
        """Monitor mouse input for recoil control"""
        while self.monitoring:
            try:
                if self.recoil_enabled and mouse.is_pressed(button='left'):
                    # Apply recoil compensation based on current settings
                    vert = self.vertical_recoil.get()
                    horiz = self.horizontal_recoil.get()
                    
                    if vert > 0 or horiz > 0:
                        # Move mouse to compensate for recoil
                        mouse.move(horiz, vert, absolute=False)
                        time.sleep(0.01)  # Small delay
                        
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(0.01)  # Small delay to prevent high CPU usage

def main():
    root = tk.Tk()
    app = EnhancedAntiRecoilApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 