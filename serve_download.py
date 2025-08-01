#!/usr/bin/env python3
"""
Simple HTTP Server for Downloading Executable
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

class DownloadHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the download page
            self.path = '/download_page.html'
        elif self.path == '/download':
            # Serve the executable file
            self.path = '/SystemDownloadManager.exe'
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="SystemDownloadManager.exe"')
            self.end_headers()
            
            # Send the executable file
            try:
                with open('SystemDownloadManager.exe', 'rb') as f:
                    self.wfile.write(f.read())
                return
            except FileNotFoundError:
                self.send_error(404, "Executable not found")
                return
        
        return super().do_GET()

def start_server():
    """Start the HTTP server"""
    PORT = 8080  # Changed to different port
    
    with socketserver.TCPServer(("", PORT), DownloadHandler) as httpd:
        print(f"🌐 Download server started at http://localhost:{PORT}")
        print(f"📥 Users can download from: http://localhost:{PORT}")
        print(f"🔗 Direct download: http://localhost:{PORT}/download")
        
        # Open browser
        webbrowser.open(f'http://localhost:{PORT}')
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

def main():
    """Main function"""
    print("🌐 System Download Manager - Download Server")
    print("=" * 50)
    
    # Check if executable exists
    if not os.path.exists("SystemDownloadManager.exe"):
        print("❌ SystemDownloadManager.exe not found!")
        print("   Please run create_exe.py first to create the executable")
        return
    
    print("✅ SystemDownloadManager.exe found")
    print("✅ download_page.html found")
    print("✅ Starting download server...")
    
    # Start server
    start_server()

if __name__ == "__main__":
    main() 