"""
Console utilities for DrGPT

Provides centralized console functionality.
"""

from rich.console import Console
from rich.markdown import Markdown

# Global console instance
console = Console()


def print_markdown(content: str) -> None:
    """Print content as markdown
    
    Args:
        content: Content to print as markdown
    """
    if content.strip():
        markdown = Markdown(content)
        console.print(markdown)


def print_error(message: str) -> None:
    """Print error message
    
    Args:
        message: Error message to print
    """
    console.print(f"[[bold red]-[/bold red]] Error: {message}")


def print_warning(message: str) -> None:
    """Print warning message
    
    Args:
        message: Warning message to print
    """
    console.print(f"[[yellow]-[/yellow]] Warning: {message}")


def print_success(message: str) -> None:
    """Print success message
    
    Args:
        message: Success message to print
    """
    console.print(f"[[green]+[/green]] {message}")
