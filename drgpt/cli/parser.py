"""
Argument parser for DrGPT CLI

Provides argument parsing functionality separated from main CLI logic.
"""

import argparse
from ..core.config import SUPPORTED_PROVIDERS


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser for DrGPT CLI
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description="DrGPT - Multi-Provider AI Assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  drgpt "Explain quantum computing"
  drgpt --code "Create a Python function to sort a list"
  drgpt -c "Create a Python function to sort a list"
  drgpt --shell "Find all Python files larger than 1MB"
  drgpt -s "Find all Python files larger than 1MB" 
  drgpt --interface  # Setup terminal aliases
  drgpt -i           # Setup terminal aliases
  drgpt --editor
  drgpt -e
  drgpt --output result.md "Explain AI"
  drgpt -o result.md "Explain AI"
  drgpt --provider openai --model gpt-4 "Complex reasoning task"
  drgpt --list-providers
  drgpt --update
  drgpt --version
  
After setup with -i, use these aliases in your terminal:
  ! "What is machine learning?"     # Chat with AI
  s: "Find Python files"            # Shell commands  
  c: "Create a function"             # Code generation
  e:                                 # Open editor
        """
    )
    
    # Main prompt argument
    parser.add_argument(
        "prompt",
        nargs="?",
        help="The prompt to send to the AI"
    )
    
    # Core functionality
    parser.add_argument(
        "--code", "-c",
        action="store_true",
        help="Generate code only in markdown format (no explanations)"
    )
    
    parser.add_argument(
        "--shell", "-s",
        action="store_true", 
        help="Generate shell commands with interactive execution options"
    )
    
    parser.add_argument(
        "--editor", "-e",
        action="store_true",
        help="Open vi text editor for input, then process with AI"
    )
    
    parser.add_argument(
        "--interface", "-i",
        action="store_true",
        help="Setup terminal aliases for DrGPT integration (!, s:, c:, e:)"
    )
    
    parser.add_argument(
        "--chat", "-ch",
        metavar="SESSION_ID",
        help="Start or continue a chat session"
    )
    
    # Provider management
    parser.add_argument(
        "--provider",
        choices=list(SUPPORTED_PROVIDERS.keys()),
        help="AI provider to use"
    )
    
    parser.add_argument(
        "--model",
        help="AI model to use"
    )
    
    parser.add_argument(
        "--api-key",
        help="Set API key for the provider"
    )
    
    parser.add_argument(
        "--list-providers",
        action="store_true",
        help="List all available providers and models"
    )
    
    parser.add_argument(
        "--list-models",
        metavar="PROVIDER",
        help="List models for a specific provider"
    )
    
    # Output options
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        help="Save response to file"
    )
    
    parser.add_argument(
        "--streaming",
        action="store_true",
        help="Enable streaming output (default)"
    )
    
    parser.add_argument(
        "--no-streaming",
        action="store_true",
        help="Disable streaming output"
    )
    
    parser.add_argument(
        "--no-markdown",
        action="store_true",
        help="Disable markdown rendering (show plain text output only)"
    )
    
    # AI parameters
    parser.add_argument(
        "--temperature",
        type=float,
        metavar="TEMP",
        help="Set temperature for AI generation (0.0-2.0)"
    )
    
    parser.add_argument(
        "--max-tokens",
        type=int,
        metavar="TOKENS",
        help="Set maximum tokens for response"
    )
    
    # Utility
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information"
    )
    
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show current configuration status"
    )
    
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update DrGPT to the latest version from PyPI/GitHub"
    )
    
    return parser


def determine_mode(args: argparse.Namespace) -> str:
    """Determine the appropriate mode based on arguments
    
    Args:
        args: Parsed command line arguments
        
    Returns:
        Mode string
    """
    if args.code:
        return "code"
    elif args.shell:
        return "shell"
    elif args.chat:
        return "chat"
    else:
        return "default"
