"""
File handling utilities for DrGPT

Provides file operation functionality.
"""

import sys
from typing import List
from .console import console, print_error, print_success


def save_response_to_file(response_chunks: List[str], output_path: str) -> None:
    """Save AI response to a file
    
    Args:
        response_chunks: List of response chunks to save
        output_path: Path to save the file
    """
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("".join(response_chunks))
        print_success(f"Response saved to {output_path}")
    except Exception as e:
        print_error(f"Error saving to file: {e}")


def read_file_content(file_path: str) -> str:
    """Read content from a file
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File content
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file can't be read
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file_content(file_path: str, content: str) -> None:
    """Write content to a file
    
    Args:
        file_path: Path to the file to write
        content: Content to write
        
    Raises:
        IOError: If file can't be written
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
