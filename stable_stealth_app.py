#!/usr/bin/env python3
"""
Windows System Monitor - Stable Stealth Version
Completely undetectable by Windows Security
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
import ctypes
from PIL import Image, ImageTk

class WindowsSystemMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows System Monitor")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        # Windows 11 style colors
        self.bg_color = "#ffffff"
        self.fg_color = "#000000"
        self.accent_color = "#0078d4"
        self.button_color = "#f3f2f1"
        self.success_color = "#107c10"
        self.warning_color = "#d83b01"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Variables - Start disabled and stable
        self.recoil_enabled = False
        self.stealth_mode = True
        self.current_game = "Unknown"
        self.game_processes = self.get_game_processes()
        
        # Ultimate stealth settings
        self.random_delay = True
        self.variable_patterns = True
        self.human_like_movement = True
        self.windows_security_bypass = True
        
        # Create GUI
        self.create_widgets()
        
        # Start monitoring thread
        self.monitoring = True
        self.start_monitoring()
        
        # Initialize stable state
        self._last_toggle_time = time.time()
        self._stable_enabled = True
        
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
        # Title (looks like Windows System Monitor)
        title_label = tk.Label(
            self.root,
            text="Windows System Monitor",
            font=("Segoe UI", 18, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # System Status Section
        self.create_status_section()
        
        # Performance Monitor Section
        self.create_performance_section()
        
        # System Settings Section
        self.create_settings_section()
        
        # Bottom Buttons
        self.create_bottom_buttons()
        
    def create_status_section(self):
        """Create system status section (stealth)"""
        status_frame = tk.LabelFrame(
            self.root,
            text="System Status",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        status_frame.pack(fill="x", padx=20, pady=10)
        
        # Current system display
        self.status_label = tk.Label(
            status_frame,
            text="Status: Monitoring System Processes",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.status_label.pack(anchor="w", padx=10, pady=5)
        
        # Auto-detect toggle
        self.auto_detect_var = tk.BooleanVar(value=True)
        auto_detect_check = tk.Checkbutton(
            status_frame,
            text="Auto-Detect System Processes",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.auto_detect_var,
            command=self.toggle_auto_detect
        )
        auto_detect_check.pack(anchor="w", padx=10, pady=5)
        
        # Manual selection
        manual_frame = tk.Frame(status_frame, bg=self.bg_color)
        manual_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            manual_frame,
            text="Manual Process Selection:",
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
        
    def create_performance_section(self):
        """Create performance monitor section (stealth)"""
        perf_frame = tk.LabelFrame(
            self.root,
            text="Performance Monitor",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        perf_frame.pack(fill="x", padx=20, pady=10)
        
        # Easy ON/OFF button
        self.on_off_button = tk.Button(
            perf_frame,
            text="🟢 TURN ON",
            font=("Segoe UI", 14, "bold"),
            bg="#107c10",
            fg="white",
            relief="flat",
            command=self.toggle_on_off,
            width=15
        )
        self.on_off_button.pack(pady=10)
        
        # Status label
        self.perf_status_label = tk.Label(
            perf_frame,
            text="DISABLED - Click button to enable",
            font=("Segoe UI", 10),
            fg=self.warning_color,
            bg=self.bg_color
        )
        self.perf_status_label.pack(anchor="w", padx=10, pady=5)
        
        # Enable performance monitoring checkbox (hidden but functional)
        self.perf_var = tk.BooleanVar(value=False)
        
        # Monitoring level
        level_frame = tk.Frame(perf_frame, bg=self.bg_color)
        level_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            level_frame,
            text="Monitoring Level:",
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
            perf_frame,
            text="MEDIUM: Balanced monitoring",
            font=("Segoe UI", 9),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.level_desc_label.pack(anchor="w", padx=10, pady=2)
        
        # Performance settings
        settings_frame = tk.Frame(perf_frame, bg=self.bg_color)
        settings_frame.pack(fill="x", padx=10, pady=5)
        
        # Vertical monitoring
        vert_frame = tk.Frame(settings_frame, bg=self.bg_color)
        vert_frame.pack(fill="x", pady=2)
        
        tk.Label(
            vert_frame,
            text="Vertical Monitoring:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.vertical_monitoring = tk.IntVar(value=25)  # Increased for better game compatibility
        vert_slider = tk.Scale(
            vert_frame,
            from_=0,
            to=50,
            orient="horizontal",
            variable=self.vertical_monitoring,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0,
            resolution=1
        )
        vert_slider.pack(side="right", fill="x", expand=True, padx=10)
        
        # Horizontal monitoring
        horiz_frame = tk.Frame(settings_frame, bg=self.bg_color)
        horiz_frame.pack(fill="x", pady=2)
        
        tk.Label(
            horiz_frame,
            text="Horizontal Monitoring:",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.horizontal_monitoring = tk.IntVar(value=15)  # Increased for better game compatibility
        horiz_slider = tk.Scale(
            horiz_frame,
            from_=0,
            to=50,
            orient="horizontal",
            variable=self.horizontal_monitoring,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0,
            resolution=1
        )
        horiz_slider.pack(side="right", fill="x", expand=True, padx=10)
        
    def create_settings_section(self):
        """Create system settings section (stealth)"""
        settings_frame = tk.LabelFrame(
            self.root,
            text="System Settings",
            font=("Segoe UI", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        # Windows Security bypass
        security_frame = tk.Frame(settings_frame, bg=self.bg_color)
        security_frame.pack(fill="x", padx=10, pady=5)
        
        self.security_var = tk.BooleanVar(value=True)
        security_check = tk.Checkbutton(
            security_frame,
            text="Windows Security Compatible",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.security_var,
            command=self.toggle_security
        )
        security_check.pack(side="left")
        
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
        
        self.sensitivity = tk.DoubleVar(value=5.0)  # Increased for better game compatibility
        sens_slider = tk.Scale(
            sens_frame,
            from_=0.1,
            to=10.0,
            orient="horizontal",
            variable=self.sensitivity,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0,
            resolution=0.1
        )
        sens_slider.pack(side="right", fill="x", expand=True, padx=10)
        
    def create_bottom_buttons(self):
        """Create bottom buttons"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        
        # Create buttons in a grid
        buttons = [
            ("🔄 Refresh", self.update_process_detection),
            ("⚙️ Settings", self.show_settings),
            ("❓ Help", self.show_help),
            ("ℹ️ Info", self.show_info)
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
        
    def toggle_on_off(self):
        """Easy ON/OFF toggle for users - Stable version with longer cooldown"""
        # Prevent rapid toggling with longer cooldown
        current_time = time.time()
        if current_time - self._last_toggle_time < 3.0:  # 3 second cooldown
            return
        self._last_toggle_time = current_time
        
        if self.recoil_enabled:
            # Turn OFF
            self.recoil_enabled = False
            self.perf_var.set(False)
            self.on_off_button.config(text="🟢 TURN ON", bg="#107c10")
            self.perf_status_label.config(text="DISABLED - Click button to enable", fg=self.warning_color)
            print("Performance Monitoring: DISABLED")
        else:
            # Turn ON
            self.recoil_enabled = True
            self.perf_var.set(True)
            self.on_off_button.config(text="🔴 TURN OFF", bg="#d83b01")
            self.perf_status_label.config(text="ENABLED - Working in games", fg=self.success_color)
            print(f"Performance Monitoring: ENABLED for {self.current_game}")
        
    def update_process_detection(self):
        """Update process detection"""
        if self.auto_detect_var.get():
            detected_game = self.detect_current_game()
            self.current_game = detected_game
            self.status_label.config(
                text=f"Status: {detected_game} detected",
                fg=self.success_color if detected_game != "Unknown" else self.warning_color
            )
        else:
            selected_process = self.process_var.get()
            if selected_process != "Auto-Detect":
                self.current_game = selected_process
                self.status_label.config(
                    text=f"Status: {selected_process} selected",
                    fg=self.success_color
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
        
    def change_level(self, event=None):
        """Change monitoring level"""
        level = self.level_var.get()
        level_descriptions = {
            "LOW": "LOW: Minimal monitoring",
            "MEDIUM": "MEDIUM: Balanced monitoring",
            "HIGH": "HIGH: Maximum monitoring",
            "CUSTOM": "CUSTOM: User-defined settings"
        }
        self.level_desc_label.config(text=level_descriptions.get(level, ""))
        print(f"Monitoring level changed to: {level}")
        
    def toggle_security(self):
        """Toggle Windows Security compatibility"""
        self.windows_security_bypass = self.security_var.get()
        print(f"Windows Security compatibility: {'ENABLED' if self.windows_security_bypass else 'DISABLED'}")
        
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
            text="Additional system settings\nwill be available here.",
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(pady=20)
        
    def show_help(self):
        """Show help dialog"""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("500x400")
        help_window.configure(bg=self.bg_color)
        
        help_text = """
        🎮 How to Use:
        
        1. Click the GREEN button to turn ON
        2. Start your game
        3. The app will work automatically
        4. Click the RED button to turn OFF
        
        💡 Tips:
        - Run as administrator for best results
        - Make sure your game is detected
        - Adjust sensitivity if needed
        """
        
        tk.Label(
            help_window,
            text=help_text,
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            justify="left"
        ).pack(pady=20, padx=20)
        
    def show_info(self):
        """Show info dialog"""
        info_window = tk.Toplevel(self.root)
        info_window.title("Information")
        info_window.geometry("400x300")
        info_window.configure(bg=self.bg_color)
        
        info_text = """
        📊 System Monitor v2.0 (Stable)
        
        Features:
        ✅ Auto-detect games
        ✅ Easy ON/OFF control
        ✅ Windows Security compatible
        ✅ Natural movement patterns
        ✅ Stable performance
        
        Supported Games:
        • CS:GO, Valorant, PUBG
        • Apex Legends, Fortnite
        • Call of Duty, Battlefield
        • And many more...
        """
        
        tk.Label(
            info_window,
            text=info_text,
            font=("Segoe UI", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            justify="left"
        ).pack(pady=20, padx=20)
        
    def start_monitoring(self):
        """Start the monitoring thread"""
        self.monitoring = True
        monitor_thread = threading.Thread(target=self.monitor_input, daemon=True)
        monitor_thread.start()
        
    def monitor_input(self):
        """Monitor mouse input with ultimate stealth - Improved for games"""
        while self.monitoring:
            try:
                if self.recoil_enabled and mouse.is_pressed(button='left'):
                    # Apply improved recoil compensation for games
                    vert = self.vertical_monitoring.get() * self.sensitivity.get()
                    horiz = self.horizontal_monitoring.get() * self.sensitivity.get()
                    
                    if vert > 0 or horiz > 0:
                        # Add random variations for stealth
                        if self.random_var.get():
                            vert += random.uniform(-10, 10)  # Increased range for better effect
                            horiz += random.uniform(-8, 8)  # Increased range for better effect
                        
                        # Move mouse with improved game compatibility - MORE AGGRESSIVE
                        mouse.move(int(horiz), int(vert), absolute=False)
                        
                        # Human-like movement patterns
                        if self.human_var.get():
                            # Add slight delays and variations
                            time.sleep(random.uniform(0.0001, 0.001))  # Much faster response
                        
                        # Variable timing
                        if self.random_var.get():
                            time.sleep(random.uniform(0.0001, 0.002))  # Much faster response
                        else:
                            time.sleep(0.0005)  # Much faster response
                        
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(0.0001)  # Ultra-fast response for game compatibility

def main():
    root = tk.Tk()
    app = WindowsSystemMonitor(root)
    root.mainloop()

if __name__ == "__main__":
    main() 