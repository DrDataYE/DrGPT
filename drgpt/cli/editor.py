"""
Editor integration for DrGPT CLI

Handles text editor integration for complex prompt composition.
"""

import subprocess
import tempfile
import os
import sys
from typing import Optional

from rich.console import Console

# Initialize rich console
console = Console()


def get_system_editor() -> str:
    """Get vi text editor (always use vi for consistency)"""
    return 'vi'


def handle_editor_input() -> str:
    """Handle editor input by opening a text editor
    
    Returns:
        The processed prompt from the editor
        
    Raises:
        SystemExit: If editor fails or user cancels
    """
    console.print("[dim]Opening text editor... Write your prompt and save/close to continue.[/dim]")
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as tmp_file:
        tmp_file.write("# Write your prompt here\n# Lines starting with # will be ignored\n\n")
        tmp_path = tmp_file.name
    
    try:
        # Get appropriate editor
        editor = get_system_editor()
        
        # Open editor
        subprocess.run([editor, tmp_path], check=True)
        
        # Read content
        with open(tmp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Filter out comments and empty lines
        lines = []
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                lines.append(line)
        
        prompt = '\n'.join(lines).strip()
        
        if not prompt:
            console.print("[[yellow]-[/yellow]] No content provided. Exiting.")
            sys.exit(0)
        
        return prompt
        
    except subprocess.CalledProcessError:
        console.print("[[bold red]-[/bold red]] Could not open text editor")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[[yellow]-[/yellow]] Cancelled by user")
        sys.exit(0)
    finally:
        # Clean up temporary file
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
