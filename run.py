#!/usr/bin/env python3
"""
QR Code Generator Startup Script

Standalone startup script for the QR Code Generator web application.
This script handles the initialization, dependency checking, and automatic
browser opening for the Flask application.

Features:
- Automatic dependency validation
- Browser auto-launch
- User-friendly error messages
- Cross-platform compatibility

Usage:
    python run.py

Author: Carlos Merino
Version: 1.0.0
"""

import os
import sys
import webbrowser
from threading import Timer

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
    
    def open_browser():
        """
        Open the default web browser to the application URL.
        
        This function is called automatically after a 1.5-second delay
        to ensure the Flask server has started before opening the browser.
        """
        webbrowser.open('http://127.0.0.1:5000')
    
    def main():
        """
        Main application startup function.
        
        Handles the complete startup process including:
        - Displaying startup information
        - Scheduling browser auto-launch
        - Starting the Flask development server
        
        The server runs with debug mode enabled and reloader disabled
        to prevent conflicts with the auto-browser opening feature.
        
        Raises:
            KeyboardInterrupt: When user presses Ctrl+C to stop the server
        """
        print("🚀 Starting QR Code Generator...")
        print("📱 Application will be available at: http://127.0.0.1:5000")
        print("🔗 Browser will open automatically...")
        print("⏹️  Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Schedule browser to open automatically after server starts
        Timer(1.5, open_browser).start()
        
        # Start the Flask application
        app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
    
    if __name__ == '__main__':
        main()
        
except ImportError as e:
    print("❌ Error: Could not import required dependencies.")
    print("💡 Solution:")
    print("   1. Make sure the virtual environment is activated:")
    print("      Windows: venv\\Scripts\\activate")
    print("      Linux/Mac: source venv/bin/activate")
    print("   2. Install the dependencies:")
    print("      pip install -r requirements.txt")
    print(f"   Specific error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    sys.exit(1) 