#!/usr/bin/env python3
"""
Simple HTTP server to serve the lung visualization application.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Add the parent directory to the path to import lung_model
sys.path.insert(0, str(Path(__file__).parent.parent))

from lung_visualization.lung_model import export_model_data

PORT = 8000

def main():
    """Start the web server and generate model data."""
    # Change to the lung_visualization directory
    os.chdir(Path(__file__).parent)
    
    # Generate the model data JSON file
    print("Generating lung model data...")
    export_model_data('lung_model_data.json')
    print(f"✓ Model data generated: lung_model_data.json")
    
    # Start the HTTP server
    Handler = http.server.SimpleHTTPRequestHandler
    
    print(f"\n{'='*60}")
    print(f"🫁 Lung Visualization Server Starting...")
    print(f"{'='*60}")
    print(f"\n📍 Server URL: http://localhost:{PORT}")
    print(f"📁 Serving from: {os.getcwd()}")
    print(f"\n💡 Open your browser and navigate to:")
    print(f"   http://localhost:{PORT}/index.html")
    print(f"\n⌨️  Press Ctrl+C to stop the server\n")
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped.")
            sys.exit(0)

if __name__ == "__main__":
    main()
