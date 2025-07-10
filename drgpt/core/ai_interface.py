"""
AI Interface Module

Provides a unified interface for different AI providers including
OpenAI, Anthropic, Google, and custom APIs.
"""

import json
import requests
from typing import Dict, List, Generator, Optional, Any
from abc import ABC, abstractmethod

from .config import config, SUPPORTED_PROVIDERS


class AIProvider(ABC):
    """Abstract base class for AI providers"""
    
    def __init__(self, api_key: str, base_url: str):
        """Initialize AI provider
        
        Args:
            api_key: API key for authentication
            base_url: Base URL for API calls
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self._setup_headers()
    
    def _setup_headers(self) -> None:
        """Setup default headers for requests"""
        self.session.headers.update({
            "User-Agent": "DrGPT/1.0.0",
            "Authorization": f"Bearer {self.api_key}"
        })
    
    @abstractmethod
    def generate_completion(self, messages: List[Dict], model: str, **kwargs) -> Generator[str, None, None]:
        """Generate completion from the AI provider
        
        Args:
            messages: List of conversation messages
            model: Model name to use
            **kwargs: Additional parameters
            
        Yields:
            Generated text chunks
        """
        pass
    
    @abstractmethod
    def get_models(self) -> List[str]:
        """Get available models for this provider
        
        Returns:
            List of model names
        """
        pass


class OpenAIProvider(AIProvider):
    """OpenAI API Provider"""
    
    def _setup_headers(self) -> None:
        """Setup OpenAI specific headers"""
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "DrGPT/1.0.0"
        })
    
    def generate_completion(self, messages: List[Dict], model: str, **kwargs) -> Generator[str, None, None]:
        """Generate streaming completion from OpenAI
        
        Args:
            messages: List of conversation messages
            model: OpenAI model name
            **kwargs: Additional parameters (temperature, max_tokens, etc.)
            
        Yields:
            Generated text chunks
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": True,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 2048),
            "top_p": kwargs.get("top_p", 1.0)
        }
        
        try:
            response = self.session.post(url, json=payload, stream=True, timeout=60)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        line = line[6:]
                        if line.strip() == '[DONE]':
                            break
                        try:
                            data = json.loads(line)
                            if 'choices' in data and len(data['choices']) > 0:
                                delta = data['choices'][0].get('delta', {})
                                content = delta.get('content', '')
                                if content:
                                    yield content
                        except json.JSONDecodeError:
                            continue
        except requests.exceptions.RequestException as e:
            yield f"Network error: {str(e)}"
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def get_models(self) -> List[str]:
        """Get available OpenAI models"""
        return SUPPORTED_PROVIDERS["openai"]["models"]


class AnthropicProvider(AIProvider):
    """Anthropic (Claude) API Provider"""
    
    def _setup_headers(self) -> None:
        """Setup Anthropic specific headers"""
        self.session.headers.update({
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "User-Agent": "DrGPT/1.0.0"
        })
    
    def generate_completion(self, messages: List[Dict], model: str, **kwargs) -> Generator[str, None, None]:
        """Generate completion from Anthropic API
        
        Args:
            messages: List of conversation messages
            model: Anthropic model name
            **kwargs: Additional parameters
            
        Yields:
            Generated text chunks
        """
        url = f"{self.base_url}/messages"
        
        # Convert messages format for Anthropic
        system_message = ""
        user_messages = []
        
        for msg in messages:
            if msg["role"] == "system":
                system_message = msg["content"]
            else:
                user_messages.append(msg)
        
        payload = {
            "model": model,
            "max_tokens": kwargs.get("max_tokens", 2048),
            "messages": user_messages,
            "stream": True
        }
        
        if system_message:
            payload["system"] = system_message
        
        try:
            response = self.session.post(url, json=payload, stream=True, timeout=60)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        line = line[6:]
                        try:
                            data = json.loads(line)
                            if data.get("type") == "content_block_delta":
                                delta = data.get("delta", {})
                                text = delta.get("text", "")
                                if text:
                                    yield text
                        except json.JSONDecodeError:
                            continue
        except requests.exceptions.RequestException as e:
            yield f"Network error: {str(e)}"
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def get_models(self) -> List[str]:
        """Get available Anthropic models"""
        return SUPPORTED_PROVIDERS["anthropic"]["models"]


class CustomProvider(AIProvider):
    """Custom API Provider (fallback)"""
    
    def generate_completion(self, messages: List[Dict], model: str, **kwargs) -> Generator[str, None, None]:
        """Generate fallback response for custom provider
        
        Args:
            messages: List of conversation messages
            model: Model name (ignored for fallback)
            **kwargs: Additional parameters (ignored)
            
        Yields:
            Fallback response
        """
        # Extract the user's message
        user_message = ""
        for msg in messages:
            if msg["role"] == "user":
                user_message = msg["content"]
                break
        
        # Generate a simple fallback response
        yield "Hello! I'm DrGPT, your AI assistant. "
        yield f"I received your message: '{user_message[:50]}...' " if len(user_message) > 50 else f"I received your message: '{user_message}' "
        yield "However, I don't have access to an AI provider right now. "
        yield "Please configure an API key for OpenAI, Anthropic, or another supported provider to get intelligent responses."
    
    def get_models(self) -> List[str]:
        """Get available custom models"""
        return ["custom-model"]


class AIInterface:
    """Main AI interface that manages different providers"""
    
    def __init__(self):
        """Initialize AI interface"""
        self.providers = {}
        self._initialize_providers()
    
    def _initialize_providers(self) -> None:
        """Initialize available providers based on configuration"""
        # OpenAI
        openai_key = config.get_api_key("openai")
        if openai_key:
            openai_config = config.get_provider_config("openai")
            self.providers["openai"] = OpenAIProvider(
                openai_key, 
                openai_config["base_url"]
            )
        
        # Anthropic
        anthropic_key = config.get_api_key("anthropic")
        if anthropic_key:
            anthropic_config = config.get_provider_config("anthropic")
            self.providers["anthropic"] = AnthropicProvider(
                anthropic_key,
                anthropic_config["base_url"]
            )
        
        # Always have custom provider as fallback
        self.providers["custom"] = CustomProvider("", "")
    
    def get_provider(self, provider_name: Optional[str] = None) -> AIProvider:
        """Get AI provider instance
        
        Args:
            provider_name: Name of provider. If None, uses default.
            
        Returns:
            AI provider instance
        """
        if provider_name is None:
            provider_name = config.get("DEFAULT_PROVIDER")
        
        if provider_name in self.providers:
            return self.providers[provider_name]
        
        # Fallback to custom provider
        return self.providers["custom"]
    
    def generate_completion(
        self,
        prompt: str,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        role: Optional[str] = None,
        **kwargs
    ) -> Generator[str, None, None]:
        """Generate completion using specified or default provider
        
        Args:
            prompt: User prompt
            provider: Provider name (optional)
            model: Model name (optional)
            role: System role (optional)
            **kwargs: Additional parameters
            
        Yields:
            Generated text chunks
        """
        if provider is None:
            provider = config.get("DEFAULT_PROVIDER")
        
        if model is None:
            model = config.get("DEFAULT_MODEL")
        
        # Build messages
        messages = []
        
        # Add system role if specified
        if role and role != "default":
            system_content = self._get_role_content(role)
            if system_content:
                messages.append({"role": "system", "content": system_content})
        
        # Add user prompt
        messages.append({"role": "user", "content": prompt})
        
        # Get provider and generate completion
        ai_provider = self.get_provider(provider)
        
        generation_params = {
            "temperature": config.get("TEMPERATURE"),
            "max_tokens": config.get("MAX_TOKENS"),
            "top_p": config.get("TOP_P"),
            **kwargs
        }
        
        yield from ai_provider.generate_completion(messages, model, **generation_params)
    
    def _get_role_content(self, role: str) -> str:
        """Get content for a specific role
        
        Args:
            role: Role name
            
        Returns:
            Role content string
        """
        # Role definitions for different modes
        if role == "code":
            return ("You are a code generation assistant. Generate ONLY code without any explanations, "
                   "comments, or descriptions. Return only the requested code in markdown format. "
                   "Do not include any text before or after the code block.")
        elif role == "shell":
            return ("You are a shell command generator. Generate ONLY the shell command needed to accomplish "
                   "the task. Return only the command without any explanations, descriptions, or additional text. "
                   "Ensure the command is safe and efficient.")
        else:
            return ""
    
    def list_providers(self) -> Dict[str, List[str]]:
        """List available providers and their models
        
        Returns:
            Dictionary mapping provider names to model lists
        """
        result = {}
        for provider_name, provider_config in SUPPORTED_PROVIDERS.items():
            result[provider_name.upper()] = provider_config["models"]
        return result


# Global AI interface instance
ai_interface = AIInterface()
