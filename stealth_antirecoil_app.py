#!/usr/bin/env python3
"""
System Download Manager - Stealth Version
Looks like a normal download utility
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import threading
import time
import keyboard
import mouse
import random
import os
import sys
import psutil
from PIL import Image, ImageTk

class StealthDownloadManager:
    def __init__(self, root):
        self.root = root
        self.root.title("System Download Manager")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Normal utility colors (looks like Windows)
        self.bg_color = "#f0f0f0"
        self.fg_color = "#000000"
        self.accent_color = "#0078d4"
        self.button_color = "#e0e0e0"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.recoil_enabled = False
        self.stealth_mode = True
        self.current_game = "Unknown"
        self.game_processes = self.get_game_processes()
        
        # Stealth settings
        self.random_delay = True
        self.variable_patterns = True
        self.human_like_movement = True
        
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
            print(f"Process detection error: {e}")
        return "Unknown"
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Title (looks like a normal download manager)
        title_label = tk.Label(
            self.root,
            text="System Download Manager",
            font=("Segoe UI", 16, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # Download Status Section
        self.create_download_section()
        
        # System Optimization Section
        self.create_optimization_section()
        
        # Settings Section
        self.create_settings_section()
        
        # Bottom Buttons
        self.create_bottom_buttons()
        
    def create_download_section(self):
        """Create download status section (stealth)"""
        download_frame = tk.LabelFrame(
            self.root,
            text="Download Status",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        download_frame.pack(fill="x", padx=20, pady=10)
        
        # Current download display
        self.download_label = tk.Label(
            download_frame,
            text="Status: Idle",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.download_label.pack(anchor="w", padx=10, pady=5)
        
        # Auto-detect toggle
        self.auto_detect_var = tk.BooleanVar(value=True)
        auto_detect_check = tk.Checkbutton(
            download_frame,
            text="Auto-Detect Downloads",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.auto_detect_var,
            command=self.toggle_auto_detect
        )
        auto_detect_check.pack(anchor="w", padx=10, pady=5)
        
        # Manual selection
        manual_frame = tk.Frame(download_frame, bg=self.bg_color)
        manual_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            manual_frame,
            text="Manual Selection:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        process_names = ["Auto-Detect"] + list(self.game_processes.keys())
        self.process_var = tk.StringVar(value="Auto-Detect")
        process_combo = ttk.Combobox(
            manual_frame,
            textvariable=self.process_var,
            values=process_names,
            state="readonly",
            font=("Segoe UI", 10),
            width=15
        )
        process_combo.pack(side="right", padx=10)
        process_combo.bind("<<ComboboxSelected>>", self.change_process)
        
        # Update process detection
        self.update_process_detection()
        
    def create_optimization_section(self):
        """Create system optimization section (stealth)"""
        opt_frame = tk.LabelFrame(
            self.root,
            text="System Optimization",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        opt_frame.pack(fill="x", padx=20, pady=10)
        
        # Enable optimization
        self.opt_var = tk.BooleanVar()
        opt_check = tk.Checkbutton(
            opt_frame,
            text="Enable System Optimization:",
            font=("Segoe UI", 12, "bold"),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.opt_var,
            command=self.toggle_optimization
        )
        opt_check.pack(anchor="w", padx=10, pady=5)
        
        # Status label
        self.status_label = tk.Label(
            opt_frame,
            text="DISABLED",
            font=("Segoe UI", 10),
            fg="#ff0000",
            bg=self.bg_color
        )
        self.status_label.pack(anchor="w", padx=30, pady=2)
        
        # Optimization level
        level_frame = tk.Frame(opt_frame, bg=self.bg_color)
        level_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            level_frame,
            text="Optimization Level:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.level_var = tk.StringVar(value="MEDIUM")
        level_combo = ttk.Combobox(
            level_frame,
            textvariable=self.level_var,
            values=["LOW", "MEDIUM", "HIGH", "CUSTOM"],
            state="readonly",
            font=("Segoe UI", 10),
            width=10
        )
        level_combo.pack(side="left", padx=10)
        level_combo.bind("<<ComboboxSelected>>", self.change_level)
        
        # Level description
        self.level_desc_label = tk.Label(
            opt_frame,
            text="MEDIUM: Balanced optimization",
            font=("Segoe UI", 9),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.level_desc_label.pack(anchor="w", padx=10, pady=2)
        
        # Optimization settings
        settings_frame = tk.Frame(opt_frame, bg=self.bg_color)
        settings_frame.pack(fill="x", padx=10, pady=5)
        
        # Vertical optimization
        vert_frame = tk.Frame(settings_frame, bg=self.bg_color)
        vert_frame.pack(fill="x", pady=2)
        
        tk.Label(
            vert_frame,
            text="Vertical Optimization:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.vertical_optimization = tk.IntVar(value=8)
        vert_slider = tk.Scale(
            vert_frame,
            from_=0,
            to=20,
            orient="horizontal",
            variable=self.vertical_optimization,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        vert_slider.pack(side="right", fill="x", expand=True, padx=10)
        
        # Horizontal optimization
        horiz_frame = tk.Frame(settings_frame, bg=self.bg_color)
        horiz_frame.pack(fill="x", pady=2)
        
        tk.Label(
            horiz_frame,
            text="Horizontal Optimization:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.horizontal_optimization = tk.IntVar(value=2)
        horiz_slider = tk.Scale(
            horiz_frame,
            from_=0,
            to=20,
            orient="horizontal",
            variable=self.horizontal_optimization,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        horiz_slider.pack(side="right", fill="x", expand=True, padx=10)
        
    def create_settings_section(self):
        """Create settings section (stealth)"""
        settings_frame = tk.LabelFrame(
            self.root,
            text="Settings",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        # Stealth mode
        stealth_frame = tk.Frame(settings_frame, bg=self.bg_color)
        stealth_frame.pack(fill="x", padx=10, pady=5)
        
        self.stealth_var = tk.BooleanVar(value=True)
        stealth_check = tk.Checkbutton(
            stealth_frame,
            text="Enable Background Mode",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.stealth_var,
            command=self.toggle_stealth
        )
        stealth_check.pack(side="left")
        
        # Random delays
        random_frame = tk.Frame(settings_frame, bg=self.bg_color)
        random_frame.pack(fill="x", padx=10, pady=5)
        
        self.random_var = tk.BooleanVar(value=True)
        random_check = tk.Checkbutton(
            random_frame,
            text="Use Variable Timing",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.random_var
        )
        random_check.pack(side="left")
        
        # Human-like movement
        human_frame = tk.Frame(settings_frame, bg=self.bg_color)
        human_frame.pack(fill="x", padx=10, pady=5)
        
        self.human_var = tk.BooleanVar(value=True)
        human_check = tk.Checkbutton(
            human_frame,
            text="Natural Patterns",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.human_var
        )
        human_check.pack(side="left")
        
        # Sensitivity adjustment
        sens_frame = tk.Frame(settings_frame, bg=self.bg_color)
        sens_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            sens_frame,
            text="Sensitivity:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.sensitivity = tk.DoubleVar(value=1.5)
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
            ("Start Download", self.toggle_optimization),
            ("Change Level", self.change_level),
            ("Check Status", self.update_process_detection),
            ("Settings", self.show_settings)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Segoe UI", 10, "bold"),
                bg=self.button_color,
                fg=self.fg_color,
                relief="flat",
                command=command
            )
            btn.grid(row=0, column=i, padx=5, pady=5, sticky="ew")
            button_frame.columnconfigure(i, weight=1)
        
    def update_process_detection(self):
        """Update process detection"""
        if self.auto_detect_var.get():
            detected_game = self.detect_current_game()
            self.current_game = detected_game
            self.download_label.config(
                text=f"Status: {detected_game} detected",
                fg="#00ff00" if detected_game != "Unknown" else "#ff0000"
            )
        else:
            selected_process = self.process_var.get()
            if selected_process != "Auto-Detect":
                self.current_game = selected_process
                self.download_label.config(
                    text=f"Status: {selected_process} selected",
                    fg="#00ff00"
                )
        
        # Update every 5 seconds
        self.root.after(5000, self.update_process_detection)
        
    def toggle_auto_detect(self):
        """Toggle auto-detection"""
        print(f"Auto-detection: {'ENABLED' if self.auto_detect_var.get() else 'DISABLED'}")
        
    def change_process(self, event=None):
        """Change selected process"""
        selected_process = self.process_var.get()
        if selected_process != "Auto-Detect":
            self.auto_detect_var.set(False)
            self.current_game = selected_process
            print(f"Process changed to: {selected_process}")
        
    def toggle_optimization(self):
        """Toggle system optimization (stealth)"""
        self.recoil_enabled = self.opt_var.get()
        if self.recoil_enabled:
            self.status_label.config(text="ENABLED", fg="#00ff00")
            print(f"System Optimization: ENABLED for {self.current_game}")
        else:
            self.status_label.config(text="DISABLED", fg="#ff0000")
            print("System Optimization: DISABLED")
            
    def change_level(self, event=None):
        """Change optimization level"""
        level = self.level_var.get()
        level_descriptions = {
            "LOW": "LOW: Minimal optimization",
            "MEDIUM": "MEDIUM: Balanced optimization",
            "HIGH": "HIGH: Maximum optimization",
            "CUSTOM": "CUSTOM: User-defined settings"
        }
        self.level_desc_label.config(text=level_descriptions.get(level, ""))
        print(f"Optimization level changed to: {level}")
        
    def toggle_stealth(self):
        """Toggle stealth mode"""
        self.stealth_mode = self.stealth_var.get()
        print(f"Background mode: {'ENABLED' if self.stealth_mode else 'DISABLED'}")
        
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Advanced Settings")
        settings_window.geometry("400x300")
        settings_window.configure(bg=self.bg_color)
        
        tk.Label(
            settings_window,
            text="Advanced Settings",
            font=("Segoe UI", 16, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        ).pack(pady=20)
        
        tk.Label(
            settings_window,
            text="Additional download settings\nwill be available here.",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(pady=20)
        
    def start_monitoring(self):
        """Start the monitoring thread"""
        self.monitoring = True
        monitor_thread = threading.Thread(target=self.monitor_input, daemon=True)
        monitor_thread.start()
        
    def monitor_input(self):
        """Monitor mouse input with stealth features"""
        while self.monitoring:
            try:
                if self.recoil_enabled and mouse.is_pressed(button='left'):
                    # Apply stealth recoil compensation for ALL weapons
                    vert = self.vertical_optimization.get() * self.sensitivity.get()
                    horiz = self.horizontal_optimization.get() * self.sensitivity.get()
                    
                    if vert > 0 or horiz > 0:
                        # Add random variations for stealth
                        if self.random_var.get():
                            vert += random.uniform(-2, 2)
                            horiz += random.uniform(-1, 1)
                        
                        # Human-like movement patterns
                        if self.human_var.get():
                            # Add slight delays and variations
                            time.sleep(random.uniform(0.003, 0.008))
                        
                        # Move mouse with stealth
                        mouse.move(int(horiz), int(vert), absolute=False)
                        
                        # Variable timing
                        if self.random_var.get():
                            time.sleep(random.uniform(0.005, 0.015))
                        else:
                            time.sleep(0.01)
                        
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(0.005)  # Faster response for better game compatibility

def main():
    root = tk.Tk()
    app = StealthDownloadManager(root)
    root.mainloop()

if __name__ == "__main__":
    main() 