#!/usr/bin/env python3
"""
Test suite for DrGPT

Run this to test basic functionality after installation.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def test_imports():
    """Test if all modules can be imported correctly"""
    print("🧪 Testing imports...")
    
    try:
        import drgpt
        print("✅ Main package imported")
    except Exception as e:
        print(f"❌ Main package import failed: {e}")
        return False
    
    try:
        from drgpt.core import config, ai_interface, manager
        print("✅ Core modules imported")
    except Exception as e:
        print(f"❌ Core modules import failed: {e}")
        return False
    
    try:
        from drgpt.cli import main
        print("✅ CLI module imported")
    except Exception as e:
        print(f"❌ CLI module import failed: {e}")
        return False
    
    return True


def test_configuration():
    """Test configuration system"""
    print("\n🔧 Testing configuration...")
    
    try:
        from drgpt.core.config import config
        
        # Test basic config access
        provider = config.get("DEFAULT_PROVIDER")
        model = config.get("DEFAULT_MODEL")
        print(f"✅ Default provider: {provider}")
        print(f"✅ Default model: {model}")
        
        # Test provider listing
        providers = config.list_providers()
        print(f"✅ Available providers: {list(providers.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False


def test_ai_interface():
    """Test AI interface (without actual API calls)"""
    print("\n🤖 Testing AI interface...")
    
    try:
        from drgpt.core.ai_interface import ai_interface
        
        # Test provider initialization
        print("✅ AI interface initialized")
        
        # Test provider listing
        providers = ai_interface.list_providers()
        print(f"✅ Available providers: {list(providers.keys())}")
        
        # Test getting a provider (should fallback to custom)
        provider = ai_interface.get_provider("custom")
        print("✅ Custom provider available as fallback")
        
        return True
    except Exception as e:
        print(f"❌ AI interface test failed: {e}")
        return False


def test_manager():
    """Test DrGPT manager"""
    print("\n📊 Testing manager...")
    
    try:
        from drgpt.core.manager import manager
        
        # Test status
        status = manager.get_status()
        print(f"✅ Current provider: {status['provider']}")
        print(f"✅ Current model: {status['model']}")
        print(f"✅ Config path: {status['config_path']}")
        
        return True
    except Exception as e:
        print(f"❌ Manager test failed: {e}")
        return False


def test_cli():
    """Test CLI functionality"""
    print("\n💻 Testing CLI...")
    
    try:
        from drgpt.cli.main import create_parser
        
        # Test parser creation
        parser = create_parser()
        print("✅ CLI parser created")
        
        # Test help generation
        help_text = parser.format_help()
        if "DrGPT" in help_text:
            print("✅ Help text generated")
        else:
            print("❌ Help text missing")
            return False
        
        return True
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
        return False


def test_version():
    """Test version information"""
    print("\n📋 Testing version...")
    
    try:
        from drgpt import __version__, __description__
        print(f"✅ Version: {__version__}")
        print(f"✅ Description: {__description__}")
        
        return True
    except Exception as e:
        print(f"❌ Version test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 DrGPT Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_configuration,
        test_ai_interface,
        test_manager,
        test_cli,
        test_version
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! DrGPT is ready to use.")
        print("\n📖 Quick start:")
        print("   1. Set API key: python -m drgpt --provider openai --api-key YOUR_KEY")
        print("   2. Ask something: python -m drgpt 'Hello, how are you?'")
        print("   3. Check providers: python -m drgpt --list-providers")
        return True
    else:
        print("💥 Some tests failed. Please check the errors above.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
