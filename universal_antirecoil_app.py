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
import psutil
from PIL import Image, ImageTk

class UniversalAntiRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Anti-Recoil Control")
        self.root.geometry("600x800")
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
        self.current_game = "Unknown"
        self.current_weapon = "default"
        self.weapons = self.load_weapons()
        self.game_processes = self.get_game_processes()
        self.auto_detect = True
        
        # Create GUI
        self.create_widgets()
        
        # Start monitoring thread
        self.monitoring = False
        self.start_monitoring()
        
    def get_game_processes(self):
        """Get list of supported game processes"""
        return {
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
    
    def detect_current_game(self):
        """Detect which game is currently running"""
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    process_name = proc.info['name'].lower()
                    for game, processes in self.game_processes.items():
                        for process in processes:
                            if process.lower() in process_name:
                                return game
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception as e:
            print(f"Game detection error: {e}")
        return "Unknown"
    
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
            text="Universal Anti-Recoil",
            font=("Arial", 28, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # Game Detection Section
        self.create_game_detection_section()
        
        # Recoil Control Section
        self.create_recoil_control_section()
        
        # Weapon Selection Section
        self.create_weapon_section()
        
        # Advanced Controls Section
        self.create_advanced_section()
        
        # Bottom Buttons
        self.create_bottom_buttons()
        
    def create_game_detection_section(self):
        """Create game detection section"""
        game_frame = tk.LabelFrame(
            self.root,
            text="Game Detection",
            font=("Arial", 14, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        game_frame.pack(fill="x", padx=20, pady=10)
        
        # Current game display
        self.game_label = tk.Label(
            game_frame,
            text="Detected Game: Unknown",
            font=("Arial", 12, "bold"),
            fg=self.warning_color,
            bg=self.bg_color
        )
        self.game_label.pack(anchor="w", padx=10, pady=5)
        
        # Auto-detect toggle
        self.auto_detect_var = tk.BooleanVar(value=True)
        auto_detect_check = tk.Checkbutton(
            game_frame,
            text="Auto-Detect Game",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.auto_detect_var,
            command=self.toggle_auto_detect
        )
        auto_detect_check.pack(anchor="w", padx=10, pady=5)
        
        # Manual game selection
        manual_frame = tk.Frame(game_frame, bg=self.bg_color)
        manual_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            manual_frame,
            text="Manual Game Selection:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        game_names = ["Auto-Detect"] + list(self.game_processes.keys())
        self.game_var = tk.StringVar(value="Auto-Detect")
        game_combo = ttk.Combobox(
            manual_frame,
            textvariable=self.game_var,
            values=game_names,
            state="readonly",
            font=("Arial", 10),
            width=20
        )
        game_combo.pack(side="right", padx=10)
        game_combo.bind("<<ComboboxSelected>>", self.change_game)
        
        # Update game detection
        self.update_game_detection()
        
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
            text="Enable Recoil Control:",
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
            text="MEDIUM: Universal recoil compensation",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.mode_desc_label.pack(anchor="w", padx=10, pady=2)
        
        # Recoil settings
        settings_frame = tk.Frame(control_frame, bg=self.bg_color)
        settings_frame.pack(fill="x", padx=10, pady=5)
        
        # Vertical recoil
        vert_frame = tk.Frame(settings_frame, bg=self.bg_color)
        vert_frame.pack(fill="x", pady=2)
        
        tk.Label(
            vert_frame,
            text="Vertical Recoil:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.vertical_recoil = tk.IntVar(value=3)
        vert_slider = tk.Scale(
            vert_frame,
            from_=0,
            to=20,
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
        horiz_frame.pack(fill="x", pady=2)
        
        tk.Label(
            horiz_frame,
            text="Horizontal Recoil:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.horizontal_recoil = tk.IntVar(value=0)
        horiz_slider = tk.Scale(
            horiz_frame,
            from_=0,
            to=20,
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
            font=("Arial", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        weapon_frame.pack(fill="x", padx=20, pady=10)
        
        # Weapon info label
        self.weapon_info_label = tk.Label(
            weapon_frame,
            text="Universal Recoil Control - Works with all weapons",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            wraplength=400
        )
        self.weapon_info_label.pack(anchor="w", padx=10, pady=5)
        
        # Weapon description
        desc_label = tk.Label(
            weapon_frame,
            text="When enabled, recoil control works automatically for all weapons in the detected game.",
            font=("Arial", 9),
            fg="#888888",
            bg=self.bg_color,
            wraplength=400
        )
        desc_label.pack(anchor="w", padx=10, pady=2)
        
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
        
        # ADS requirement
        ads_frame = tk.Frame(advanced_frame, bg=self.bg_color)
        ads_frame.pack(fill="x", padx=10, pady=5)
        
        self.ads_var = tk.BooleanVar()
        ads_check = tk.Checkbutton(
            ads_frame,
            text="Require ADS (Aim Down Sights)",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.ads_var
        )
        ads_check.pack(side="left")
        
        # Sensitivity adjustment
        sens_frame = tk.Frame(advanced_frame, bg=self.bg_color)
        sens_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            sens_frame,
            text="Sensitivity Multiplier:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.sensitivity = tk.DoubleVar(value=1.0)
        sens_slider = tk.Scale(
            sens_frame,
            from_=0.1,
            to=3.0,
            orient="horizontal",
            variable=self.sensitivity,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        sens_slider.pack(side="right", fill="x", expand=True, padx=10)
        
    def create_bottom_buttons(self):
        """Create bottom buttons"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        
        # Create buttons in a grid
        buttons = [
            ("Toggle Recoil", self.toggle_recoil),
            ("Change Mode", self.change_mode),
            ("Detect Game", self.update_game_detection),
            ("Settings", self.show_settings)
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
        
    def update_game_detection(self):
        """Update game detection"""
        if self.auto_detect_var.get():
            detected_game = self.detect_current_game()
            self.current_game = detected_game
            self.game_label.config(
                text=f"Detected Game: {detected_game}",
                fg=self.success_color if detected_game != "Unknown" else self.warning_color
            )
        else:
            selected_game = self.game_var.get()
            if selected_game != "Auto-Detect":
                self.current_game = selected_game
                self.game_label.config(
                    text=f"Selected Game: {selected_game}",
                    fg=self.success_color
                )
        
        # Update every 5 seconds
        self.root.after(5000, self.update_game_detection)
        
    def toggle_auto_detect(self):
        """Toggle auto-detection"""
        self.auto_detect = self.auto_detect_var.get()
        if self.auto_detect:
            self.game_var.set("Auto-Detect")
        print(f"Auto-detection: {'ENABLED' if self.auto_detect else 'DISABLED'}")
        
    def change_game(self, event=None):
        """Change selected game"""
        selected_game = self.game_var.get()
        if selected_game != "Auto-Detect":
            self.auto_detect_var.set(False)
            self.current_game = selected_game
            print(f"Game changed to: {selected_game}")
        
    def toggle_recoil(self):
        """Toggle recoil control"""
        self.recoil_enabled = self.enable_var.get()
        if self.recoil_enabled:
            self.status_label.config(text="ON", fg=self.success_color)
            print(f"Recoil Control: ENABLED for {self.current_game}")
        else:
            self.status_label.config(text="OFF", fg=self.warning_color)
            print("Recoil Control: DISABLED")
            
    def change_mode(self, event=None):
        """Change recoil mode"""
        mode = self.mode_var.get()
        mode_descriptions = {
            "LOW": "LOW: Light recoil compensation",
            "MEDIUM": "MEDIUM: Universal recoil compensation",
            "HIGH": "HIGH: Strong recoil compensation",
            "CUSTOM": "CUSTOM: User-defined settings"
        }
        self.mode_desc_label.config(text=mode_descriptions.get(mode, ""))
        print(f"Mode changed to: {mode}")
        
    def change_weapon(self, event=None):
        """Change selected weapon (deprecated - now universal)"""
        print("Universal recoil control - works with all weapons")
        
    def update_weapon_info(self):
        """Update weapon information display (deprecated - now universal)"""
        self.weapon_info_label.config(text="Universal Recoil Control - Works with all weapons")
            
    def toggle_lua_integration(self):
        """Toggle Lua script integration"""
        if self.lua_var.get():
            try:
                if os.path.exists("enhanced_no_recoil.lua"):
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
            
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Advanced Settings")
        settings_window.geometry("400x300")
        settings_window.configure(bg=self.bg_color)
        
        tk.Label(
            settings_window,
            text="Advanced Settings",
            font=("Arial", 16, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        ).pack(pady=20)
        
        # Add more settings here
        tk.Label(
            settings_window,
            text="Game-specific settings and advanced options\nwill be available here.",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(pady=20)
        
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
                    # Apply recoil compensation for ALL weapons
                    vert = self.vertical_recoil.get() * self.sensitivity.get()
                    horiz = self.horizontal_recoil.get() * self.sensitivity.get()
                    
                    if vert > 0 or horiz > 0:
                        # Move mouse to compensate for recoil
                        mouse.move(int(horiz), int(vert), absolute=False)
                        time.sleep(0.01)  # Small delay
                        
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(0.01)  # Small delay to prevent high CPU usage

def main():
    root = tk.Tk()
    app = UniversalAntiRecoilApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 