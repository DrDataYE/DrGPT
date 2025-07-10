"""
Code mode for DrGPT

Handles code generation functionality.
"""

from .base import BaseMode


class CodeMode(BaseMode):
    """Code generation mode for DrGPT"""
    
    def process_prompt(self, prompt: str, **kwargs) -> str:
        """Process prompt for code mode
        
        Args:
            prompt: The user prompt
            **kwargs: Additional arguments
            
        Returns:
            Modified prompt for code generation
        """
        return f"Generate only code for the following request. Return only the code in markdown format without any explanations or descriptions:\n\n{prompt}"
    
    def handle_response(self, response: str, **kwargs) -> None:
        """Handle code generation response
        
        Args:
            response: The AI response containing code
            **kwargs: Additional arguments
        """
        # Code mode doesn't need special response handling
        # The response is already processed by the main query handler
        pass
