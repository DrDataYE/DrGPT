"""
DrGPT Manager

Main manager class that coordinates between different components
of the DrGPT system.
"""

from typing import Optional, Dict, Any, Generator
from pathlib import Path

from .config import config
from .ai_interface import ai_interface


class DrGPTManager:
    """Main DrGPT manager class"""
    
    def __init__(self):
        """Initialize DrGPT manager"""
        self.config = config
        self.ai = ai_interface
        self._handlers = {}
    
    def query(
        self,
        prompt: str,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        mode: str = "default",
        **kwargs
    ) -> Generator[str, None, None]:
        """Execute a query using the AI interface
        
        Args:
            prompt: User prompt
            provider: AI provider to use
            model: AI model to use
            mode: Query mode (default, code, shell, etc.)
            **kwargs: Additional parameters
            
        Yields:
            Generated response chunks
        """
        # Determine role based on mode
        role = self._get_role_for_mode(mode)
        
        # Generate completion
        yield from self.ai.generate_completion(
            prompt=prompt,
            provider=provider,
            model=model,
            role=role,
            **kwargs
        )
    
    def _get_role_for_mode(self, mode: str) -> str:
        """Get appropriate role for the given mode
        
        Args:
            mode: Query mode
            
        Returns:
            Role string
        """
        mode_to_role = {
            "code": "code",
            "shell": "shell",
            "default": "default"
        }
        return mode_to_role.get(mode, "default")
    
    def set_provider(
        self,
        provider: str,
        model: Optional[str] = None,
        api_key: Optional[str] = None
    ) -> None:
        """Set AI provider configuration
        
        Args:
            provider: Provider name
            model: Model name (optional)
            api_key: API key (optional)
        """
        if api_key:
            provider_config = self.config.get_provider_config(provider)
            api_key_env = provider_config["api_key_env"]
            self.config.set(api_key_env, api_key)
        
        self.config.set_provider(provider, model)
        
        # Reinitialize AI interface to pick up new settings
        self.ai._initialize_providers()
    
    def list_providers(self) -> Dict[str, Any]:
        """List available providers and models
        
        Returns:
            Dictionary of provider information
        """
        return self.ai.list_providers()
    
    def get_status(self) -> Dict[str, Any]:
        """Get current DrGPT status
        
        Returns:
            Status information dictionary
        """
        current_provider = self.config.get("DEFAULT_PROVIDER")
        current_model = self.config.get("DEFAULT_MODEL")
        has_api_key = bool(self.config.get_api_key(current_provider))
        
        return {
            "provider": current_provider,
            "model": current_model,
            "has_api_key": has_api_key,
            "config_path": str(self.config.config_path),
            "available_providers": list(self.config.list_providers().keys())
        }


# Global manager instance
manager = DrGPTManager()
