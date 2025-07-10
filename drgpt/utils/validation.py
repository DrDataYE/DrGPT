"""
Input validation utilities for DrGPT

Provides validation functions for user inputs.
"""

from typing import Optional


def validate_temperature(temperature: Optional[float]) -> Optional[float]:
    """Validate temperature parameter
    
    Args:
        temperature: Temperature value to validate
        
    Returns:
        Validated temperature or None if invalid
        
    Raises:
        ValueError: If temperature is out of valid range
    """
    if temperature is None:
        return None
    
    if not 0.0 <= temperature <= 2.0:
        raise ValueError("Temperature must be between 0.0 and 2.0")
    
    return temperature


def validate_max_tokens(max_tokens: Optional[int]) -> Optional[int]:
    """Validate max_tokens parameter
    
    Args:
        max_tokens: Maximum tokens value to validate
        
    Returns:
        Validated max_tokens or None if invalid
        
    Raises:
        ValueError: If max_tokens is invalid
    """
    if max_tokens is None:
        return None
    
    if max_tokens <= 0:
        raise ValueError("max_tokens must be a positive integer")
    
    if max_tokens > 100000:  # Reasonable upper limit
        raise ValueError("max_tokens is too large (max: 100000)")
    
    return max_tokens


def validate_provider(provider: str, supported_providers: dict) -> str:
    """Validate provider name
    
    Args:
        provider: Provider name to validate
        supported_providers: Dictionary of supported providers
        
    Returns:
        Validated provider name
        
    Raises:
        ValueError: If provider is not supported
    """
    if provider not in supported_providers:
        raise ValueError(f"Unsupported provider '{provider}'. Available: {', '.join(supported_providers.keys())}")
    
    return provider
