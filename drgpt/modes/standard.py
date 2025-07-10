"""
Standard mode for DrGPT

Handles normal AI interaction without special modifications.
"""

from .base import BaseMode


class StandardMode(BaseMode):
    """Standard interaction mode for DrGPT"""
    
    def process_prompt(self, prompt: str, **kwargs) -> str:
        """Process prompt for standard mode
        
        Args:
            prompt: The user prompt
            **kwargs: Additional arguments
            
        Returns:
            Unmodified prompt
        """
        return prompt
    
    def handle_response(self, response: str, **kwargs) -> None:
        """Handle standard mode response
        
        Args:
            response: The AI response
            **kwargs: Additional arguments
        """
        # Standard mode doesn't need special response handling
        pass
