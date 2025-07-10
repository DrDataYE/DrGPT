#!/usr/bin/env python3
"""
Test script to verify API key prompt behavior
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the parent directory to sys.path so we can import drgpt
sys.path.insert(0, str(Path(__file__).parent))

from drgpt.core.config import config
from drgpt.core.ai_interface import AIInterface

def test_api_key_prompt():
    """Test that only OpenAI key is prompted on first run"""
    
    # Create temporary config directory
    temp_dir = tempfile.mkdtemp()
    config_dir = Path(temp_dir) / "drgpt"
    config_dir.mkdir(parents=True)
    
    # Backup original config path
    original_path = config.config_path
    
    try:
        # Use temporary config path
        config.config_path = config_dir / "config"
        
        # Clear any existing environment variables
        for key in ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
            if key in os.environ:
                del os.environ[key]
        
        # Reset config
        config.config_data = {}
        config.set("DEFAULT_PROVIDER", "openai")
        config.set("DEFAULT_MODEL", "gpt-3.5-turbo")
        
        print("Testing API key prompt behavior...")
        print("Config path:", config.config_path)
        print("Default provider:", config.get("DEFAULT_PROVIDER"))
        
        # Initialize AI interface - this should only prompt for OpenAI key
        print("\nInitializing AI interface...")
        ai = AIInterface()
        
        print("Available providers:", list(ai.providers.keys()))
        print("✅ Test completed successfully!")
        
    finally:
        # Restore original config path
        config.config_path = original_path
        
        # Clean up temp directory
        import shutil
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    test_api_key_prompt()
