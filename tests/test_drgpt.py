#!/usr/bin/env python3
"""
Quick test script for DrGPT
Run this to test basic functionality
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from src.config import cfg
        print("✅ Config module imported")
    except Exception as e:
        print(f"❌ Config import failed: {e}")
        return False
    
    try:
        from src.ai_interface import ai
        print("✅ AI interface imported")
    except Exception as e:
        print(f"❌ AI interface import failed: {e}")
        return False
    
    try:
        from src.role import get_role_content
        print("✅ Role module imported")
    except Exception as e:
        print(f"❌ Role import failed: {e}")
        return False
    
    try:
        from src.handlers.default_handler import DefaultHandler
        print("✅ Default handler imported")
    except Exception as e:
        print(f"❌ Default handler import failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration system"""
    print("\n🔧 Testing configuration...")
    
    try:
        from src.config import cfg
        
        # Test basic config access
        provider = cfg.get("DEFAULT_PROVIDER")
        print(f"✅ Default provider: {provider}")
        
        # Test provider listing
        providers = cfg.list_providers()
        print(f"✅ Available providers: {list(providers.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False

def test_basic_functionality():
    """Test basic AI functionality with mock data"""
    print("\n🤖 Testing basic functionality...")
    
    try:
        from src.handlers.default_handler import DefaultHandler
        
        # Create handler
        handler = DefaultHandler("default")
        print("✅ Handler created")
        
        # Test message creation
        message = handler.make_messages("Test prompt")
        print(f"✅ Message created: {message[:50]}...")
        
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 DrGPT Quick Test\n")
    
    success = True
    
    # Test imports
    success &= test_imports()
    
    # Test configuration
    success &= test_config()
    
    # Test basic functionality
    success &= test_basic_functionality()
    
    print("\n" + "="*50)
    
    if success:
        print("🎉 All tests passed! DrGPT is working correctly.")
        print("\n📝 Next steps:")
        print("1. Set your API key: python main.py --provider openai --api-key YOUR_KEY")
        print("2. List providers: python main.py --list-providers")
        print("3. Ask something: python main.py 'Hello, how are you?'")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\n🔧 Try:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run initialization: python init_project.py")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
