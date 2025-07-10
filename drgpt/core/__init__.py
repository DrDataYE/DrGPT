"""Core module initialization"""

from .config import Config, config, SUPPORTED_PROVIDERS
from .ai_interface import AIInterface, ai_interface
from .manager import DrGPTManager, manager

__all__ = [
    "Config", "config", "SUPPORTED_PROVIDERS",
    "AIInterface", "ai_interface", 
    "DrGPTManager", "manager"
]
