"""
Base mode class for DrGPT

Provides the foundation for all operational modes.
"""

from abc import ABC, abstractmethod


class BaseMode(ABC):
    """Base class for all DrGPT modes"""
    
    def __init__(self, manager):
        """Initialize the mode
        
        Args:
            manager: The AI manager instance
        """
        self.manager = manager
    
    @abstractmethod
    def process_prompt(self, prompt: str, **kwargs) -> str:
        """Process a prompt according to this mode's logic
        
        Args:
            prompt: The user prompt
            **kwargs: Additional arguments
            
        Returns:
            Modified prompt for the AI
        """
        pass
    
    @abstractmethod
    def handle_response(self, response: str, **kwargs) -> None:
        """Handle the AI response according to this mode's logic
        
        Args:
            response: The AI response
            **kwargs: Additional arguments
        """
        pass
    
    def get_mode_name(self) -> str:
        """Get the name of this mode
        
        Returns:
            Mode name
        """
        return self.__class__.__name__.replace('Mode', '').lower()
