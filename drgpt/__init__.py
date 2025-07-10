"""
DrGPT - Multi-Provider AI Assistant

A powerful command-line AI assistant that supports multiple AI providers
including OpenAI, Anthropic, Google, and custom APIs.
"""

__version__ = "2.2.0"
__author__ = "DrGPT Contributors"
__license__ = "MIT"
__description__ = "Multi-Provider AI Assistant for developers and power users"

from .core.config import Config, config
from .core.ai_interface import AIInterface, ai_interface
from .core.manager import DrGPTManager, manager

__all__ = [
    "Config", "config", 
    "AIInterface", "ai_interface", 
    "DrGPTManager", "manager",
    "__version__", "__description__"
]
