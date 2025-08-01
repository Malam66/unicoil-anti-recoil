import tkinter as tk
from tkinter import ttk, messagebox
import json
import threading
import time
import keyboard
import mouse
from PIL import Image, ImageTk
import os

class AntiRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UniCoil - Anti Recoil Control")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Dark theme colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.accent_color = "#ffd700"  # Gold
        self.button_color = "#333333"
        self.button_hover = "#444444"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.recoil_enabled = False
        self.rapid_fire_enabled = False
        self.ads_required = False
        self.recoil_strength = tk.DoubleVar(value=0)
        self.recoil_delay = tk.DoubleVar(value=0)
        self.rapid_fire_speed = tk.DoubleVar(value=0)
        self.current_weapon = "default"
        self.weapons = self.load_weapons()
        
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
            text="UniCoil",
            font=("Arial", 24, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=20)
        
        # Configuration Section
        self.create_config_section()
        
        # Anti-Recoil Section
        self.create_recoil_section()
        
        # Rapid Fire Section
        self.create_rapid_fire_section()
        
        # Bottom Buttons
        self.create_bottom_buttons()
        
        # Update labels after all widgets are created
        self.update_labels()
        
    def create_config_section(self):
        """Create configuration section"""
        config_frame = tk.LabelFrame(
            self.root,
            text="CONFIGURATION",
            font=("Arial", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        config_frame.pack(fill="x", padx=20, pady=10)
        
        # Load/Save buttons
        button_frame = tk.Frame(config_frame, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        load_btn = tk.Button(
            button_frame,
            text="LOAD CONFIG",
            font=("Arial", 10, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.load_config
        )
        load_btn.pack(side="left", padx=5)
        
        save_btn = tk.Button(
            button_frame,
            text="SAVE CONFIG",
            font=("Arial", 10, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.save_config
        )
        save_btn.pack(side="left", padx=5)
        
        # Config slot selector
        slot_frame = tk.Frame(config_frame, bg=self.bg_color)
        slot_frame.pack(pady=5)
        
        tk.Label(
            slot_frame,
            text="Slot:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(side="left")
        
        self.slot_var = tk.StringVar(value="1")
        slot_spinbox = tk.Spinbox(
            slot_frame,
            from_=1,
            to=10,
            width=5,
            textvariable=self.slot_var,
            font=("Arial", 10),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat"
        )
        slot_spinbox.pack(side="left", padx=5)
        
    def create_recoil_section(self):
        """Create anti-recoil section"""
        recoil_frame = tk.LabelFrame(
            self.root,
            text="ANTI-RECOIL",
            font=("Arial", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        recoil_frame.pack(fill="x", padx=20, pady=10)
        
        # Toggle recoil script
        self.recoil_toggle = tk.BooleanVar()
        recoil_check = tk.Checkbutton(
            recoil_frame,
            text="TOGGLE RECOIL SCRIPT",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.recoil_toggle,
            command=self.toggle_recoil
        )
        recoil_check.pack(anchor="w", padx=10, pady=5)
        
        # ADS requirement
        self.ads_toggle = tk.BooleanVar()
        ads_check = tk.Checkbutton(
            recoil_frame,
            text="REQUIRE ADS (Aim Down Sight)",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.ads_toggle
        )
        ads_check.pack(anchor="w", padx=10, pady=5)
        
        # Strength slider
        strength_frame = tk.Frame(recoil_frame, bg=self.bg_color)
        strength_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            strength_frame,
            text="STRENGTH:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(anchor="w")
        
        strength_slider = tk.Scale(
            strength_frame,
            from_=0,
            to=10,
            orient="horizontal",
            variable=self.recoil_strength,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        strength_slider.pack(fill="x", pady=2)
        
        # Strength value display
        self.strength_label = tk.Label(
            strength_frame,
            text="0",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.strength_label.pack(anchor="w")
        
        # Delay slider
        delay_frame = tk.Frame(recoil_frame, bg=self.bg_color)
        delay_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            delay_frame,
            text="DELAY:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(anchor="w")
        
        delay_slider = tk.Scale(
            delay_frame,
            from_=0,
            to=200,
            orient="horizontal",
            variable=self.recoil_delay,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        delay_slider.pack(fill="x", pady=2)
        
        # Delay value display
        self.delay_label = tk.Label(
            delay_frame,
            text="0",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.delay_label.pack(anchor="w")
        
    def create_rapid_fire_section(self):
        """Create rapid fire section"""
        rapid_frame = tk.LabelFrame(
            self.root,
            text="RAPID FIRE",
            font=("Arial", 12, "bold"),
            fg=self.accent_color,
            bg=self.bg_color,
            bd=2,
            relief="solid"
        )
        rapid_frame.pack(fill="x", padx=20, pady=10)
        
        # Toggle rapid fire script
        self.rapid_toggle = tk.BooleanVar()
        rapid_check = tk.Checkbutton(
            rapid_frame,
            text="TOGGLE RAPID FIRE SCRIPT",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.rapid_toggle,
            command=self.toggle_rapid_fire
        )
        rapid_check.pack(anchor="w", padx=10, pady=5)
        
        # ADS requirement for rapid fire
        self.rapid_ads_toggle = tk.BooleanVar()
        rapid_ads_check = tk.Checkbutton(
            rapid_frame,
            text="REQUIRE ADS (aim down sight)",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color,
            selectcolor=self.button_color,
            variable=self.rapid_ads_toggle
        )
        rapid_ads_check.pack(anchor="w", padx=10, pady=5)
        
        # Speed slider
        speed_frame = tk.Frame(rapid_frame, bg=self.bg_color)
        speed_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(
            speed_frame,
            text="SPEED:",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        ).pack(anchor="w")
        
        speed_slider = tk.Scale(
            speed_frame,
            from_=0,
            to=20,
            orient="horizontal",
            variable=self.rapid_fire_speed,
            bg=self.bg_color,
            fg=self.fg_color,
            troughcolor=self.button_color,
            highlightthickness=0
        )
        speed_slider.pack(fill="x", pady=2)
        
        # Speed value display
        self.speed_label = tk.Label(
            speed_frame,
            text="0",
            font=("Arial", 10),
            fg=self.fg_color,
            bg=self.bg_color
        )
        self.speed_label.pack(anchor="w")
        
    def create_bottom_buttons(self):
        """Create bottom buttons"""
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        
        options_btn = tk.Button(
            button_frame,
            text="OPTIONS",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.show_options
        )
        options_btn.pack(side="left", fill="x", expand=True, padx=5)
        
        exit_btn = tk.Button(
            button_frame,
            text="EXIT",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.root.quit
        )
        exit_btn.pack(side="right", fill="x", expand=True, padx=5)
        
    def update_labels(self):
        """Update value labels"""
        self.strength_label.config(text=str(int(self.recoil_strength.get())))
        self.delay_label.config(text=str(int(self.recoil_delay.get())))
        self.speed_label.config(text=str(int(self.rapid_fire_speed.get())))
        self.root.after(100, self.update_labels)
        
    def toggle_recoil(self):
        """Toggle recoil script"""
        self.recoil_enabled = self.recoil_toggle.get()
        status = "ENABLED" if self.recoil_enabled else "DISABLED"
        print(f"Recoil Script: {status}")
        
    def toggle_rapid_fire(self):
        """Toggle rapid fire script"""
        self.rapid_fire_enabled = self.rapid_toggle.get()
        status = "ENABLED" if self.rapid_fire_enabled else "DISABLED"
        print(f"Rapid Fire Script: {status}")
        
    def load_config(self):
        """Load configuration from file"""
        try:
            slot = self.slot_var.get()
            filename = f"config_slot_{slot}.json"
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    config = json.load(f)
                # Apply loaded config
                self.recoil_strength.set(config.get('recoil_strength', 0))
                self.recoil_delay.set(config.get('recoil_delay', 0))
                self.rapid_fire_speed.set(config.get('rapid_fire_speed', 0))
                self.recoil_toggle.set(config.get('recoil_enabled', False))
                self.rapid_toggle.set(config.get('rapid_fire_enabled', False))
                messagebox.showinfo("Success", f"Configuration loaded from slot {slot}")
            else:
                messagebox.showwarning("Warning", f"No configuration found in slot {slot}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load configuration: {str(e)}")
            
    def save_config(self):
        """Save configuration to file"""
        try:
            slot = self.slot_var.get()
            filename = f"config_slot_{slot}.json"
            config = {
                'recoil_strength': self.recoil_strength.get(),
                'recoil_delay': self.recoil_delay.get(),
                'rapid_fire_speed': self.rapid_fire_speed.get(),
                'recoil_enabled': self.recoil_toggle.get(),
                'rapid_fire_enabled': self.rapid_toggle.get()
            }
            with open(filename, 'w') as f:
                json.dump(config, f, indent=2)
            messagebox.showinfo("Success", f"Configuration saved to slot {slot}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")
            
    def show_options(self):
        """Show options dialog"""
        options_window = tk.Toplevel(self.root)
        options_window.title("Options")
        options_window.geometry("300x200")
        options_window.configure(bg=self.bg_color)
        
        tk.Label(
            options_window,
            text="Advanced Options",
            font=("Arial", 16, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        ).pack(pady=20)
        
        # Add more options here as needed
        tk.Label(
            options_window,
            text="More options coming soon...",
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
                    # Apply recoil compensation
                    strength = int(self.recoil_strength.get())
                    delay = int(self.recoil_delay.get())
                    
                    if strength > 0:
                        # Move mouse down to compensate for recoil
                        mouse.move(0, strength, absolute=False)
                        time.sleep(delay / 1000.0)  # Convert to seconds
                        
                if self.rapid_fire_enabled and mouse.is_pressed(button='left'):
                    # Rapid fire functionality
                    speed = int(self.rapid_fire_speed.get())
                    if speed > 0:
                        # Simulate rapid clicking
                        mouse.click(button='left')
                        time.sleep(1.0 / speed)  # Adjust timing based on speed
                        
            except Exception as e:
                print(f"Monitoring error: {e}")
                
            time.sleep(0.01)  # Small delay to prevent high CPU usage

def main():
    root = tk.Tk()
    app = AntiRecoilApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 