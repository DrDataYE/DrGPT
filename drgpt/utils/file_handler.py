"""
File handling utilities for DrGPT

Provides file operation functionality.
"""

import sys
from typing import List
from .console import console, print_error, print_success


def save_response_to_file(response_chunks: List[str], output_path: str, is_code_mode: bool = False, is_shell_mode: bool = False) -> None:
    """Save AI response to a file
    
    Args:
        response_chunks: List of response chunks to save
        output_path: Path to save the file
        is_code_mode: Whether this is code mode (removes markdown code blocks)
        is_shell_mode: Whether this is shell mode (removes markdown formatting)
    """
    try:
        content = "".join(response_chunks)
        
        # Remove markdown formatting for code and shell modes
        if is_code_mode or is_shell_mode:
            content = _strip_markdown_formatting(content)
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print_success(f"Response saved to {output_path}")
    except Exception as e:
        print_error(f"Error saving to file: {e}")


def _strip_markdown_formatting(content: str) -> str:
    """Remove markdown code blocks and formatting from content
    
    Args:
        content: Content with markdown formatting
        
    Returns:
        Content without markdown formatting
    """
    import re
    
    # Remove markdown code blocks (```language\ncode\n```)
    # This pattern matches code blocks with optional language specification
    code_block_pattern = r'```(?:[a-zA-Z]*\n)?(.*?)```'
    matches = re.findall(code_block_pattern, content, flags=re.DOTALL)
    
    if matches:
        # If we found code blocks, return just the code content
        return '\n'.join(matches).strip()
    
    # If no code blocks found, clean up other markdown formatting
    # Remove inline code backticks
    content = re.sub(r'`([^`]+)`', r'\1', content)
    
    # Remove bold and italic formatting
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # **bold**
    content = re.sub(r'\*([^*]+)\*', r'\1', content)      # *italic*
    content = re.sub(r'__([^_]+)__', r'\1', content)      # __bold__
    content = re.sub(r'_([^_]+)_', r'\1', content)        # _italic_
    
    # Remove headers (# ## ###)
    content = re.sub(r'^#+\s*(.*)$', r'\1', content, flags=re.MULTILINE)
    
    # Clean up extra whitespace while preserving code structure
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Multiple empty lines to double newlines
    content = content.strip()
    
    return content


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
