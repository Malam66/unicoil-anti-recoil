#!/usr/bin/env python3
"""
UniCoil Anti-Recoil Application Launcher
Choose between basic, enhanced, universal, and stealth versions
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UniCoil Launcher")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Dark theme colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.accent_color = "#ffd700"
        self.button_color = "#333333"
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        """Create launcher GUI"""
        # Title
        title_label = tk.Label(
            self.root,
            text="UniCoil Launcher",
            font=("Arial", 24, "bold"),
            fg=self.accent_color,
            bg=self.bg_color
        )
        title_label.pack(pady=30)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Choose your anti-recoil application",
            font=("Arial", 12),
            fg=self.fg_color,
            bg=self.bg_color
        )
        subtitle_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        # Stealth version button (recommended)
        stealth_btn = tk.Button(
            button_frame,
            text="Stealth Version\n(Undetectable - Recommended)",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg=self.fg_color,
            relief="flat",
            command=self.launch_stealth,
            width=25,
            height=3
        )
        stealth_btn.pack(pady=10)
        
        # Universal version button
        universal_btn = tk.Button(
            button_frame,
            text="Universal Version\n(All Games)",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg=self.fg_color,
            relief="flat",
            command=self.launch_universal,
            width=25,
            height=3
        )
        universal_btn.pack(pady=5)
        
        # Basic version button
        basic_btn = tk.Button(
            button_frame,
            text="Basic Version\n(Simple Interface)",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.launch_basic,
            width=25,
            height=3
        )
        basic_btn.pack(pady=5)
        
        # Enhanced version button
        enhanced_btn = tk.Button(
            button_frame,
            text="Enhanced Version\n(Advanced Features)",
            font=("Arial", 12, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            relief="flat",
            command=self.launch_enhanced,
            width=25,
            height=3
        )
        enhanced_btn.pack(pady=5)
        
        # Exit button
        exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Arial", 10),
            bg="#ff4444",
            fg=self.fg_color,
            relief="flat",
            command=self.root.quit,
            width=10
        )
        exit_btn.pack(pady=20)
        
    def launch_stealth(self):
        """Launch stealth version"""
        try:
            if os.path.exists("stealth_antirecoil_app.py"):
                subprocess.Popen([sys.executable, "stealth_antirecoil_app.py"])
                self.root.withdraw()  # Hide launcher
            else:
                messagebox.showerror("Error", "stealth_antirecoil_app.py not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch stealth version: {str(e)}")
        
    def launch_universal(self):
        """Launch universal version"""
        try:
            if os.path.exists("universal_antirecoil_app.py"):
                subprocess.Popen([sys.executable, "universal_antirecoil_app.py"])
                self.root.withdraw()  # Hide launcher
            else:
                messagebox.showerror("Error", "universal_antirecoil_app.py not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch universal version: {str(e)}")
        
    def launch_basic(self):
        """Launch basic version"""
        try:
            if os.path.exists("anti_recoil_app.py"):
                subprocess.Popen([sys.executable, "anti_recoil_app.py"])
                self.root.withdraw()  # Hide launcher
            else:
                messagebox.showerror("Error", "anti_recoil_app.py not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch basic version: {str(e)}")
            
    def launch_enhanced(self):
        """Launch enhanced version"""
        try:
            if os.path.exists("enhanced_antirecoil_app.py"):
                subprocess.Popen([sys.executable, "enhanced_antirecoil_app.py"])
                self.root.withdraw()  # Hide launcher
            else:
                messagebox.showerror("Error", "enhanced_antirecoil_app.py not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch enhanced version: {str(e)}")

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import keyboard
        import mouse
        import tkinter
        import psutil
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main function"""
    print("UniCoil Launcher Starting...")
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    # Create and run launcher
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 