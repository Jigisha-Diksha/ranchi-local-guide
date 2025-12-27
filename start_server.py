#!/usr/bin/env python3
"""
Simple script to start the Ranchi Translator web server
"""

import os
import sys
from app import app

def main():
    print("🚀 Starting Ranchi Local Guide Translator Web Server...")
    print("=" * 60)
    
    try:
        # Check if translator is working
        from ranchi_translator import RanchiTranslator
        translator = RanchiTranslator()
        print(f"✅ Translator loaded with {len(translator.terms_dict)} terms")
        
        print("\n🌐 Server will be available at:")
        print("   • Local:    http://localhost:5000")
        print("   • Network:  http://0.0.0.0:5000")
        print("\n💡 Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Start the Flask server
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=False  # Disable reloader to avoid issues
        )
        
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thanks for using Ranchi Translator!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("   • Make sure Flask is installed: pip install flask")
        print("   • Check if port 5000 is available")
        print("   • Verify all files are in the correct location")

if __name__ == "__main__":
    main()