"""
Command Line Interface for DrGPT

Provides the main CLI functionality for DrGPT.
"""

import sys

from .parser import create_parser
from .commands import handle_list_providers, handle_list_models, handle_status, handle_version
from .interface import handle_interactive_interface
from .editor import handle_editor_input
from .query_handler import handle_query
from ..core.updater import handle_update_command
from ..utils.console import print_error


def main() -> None:
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle special commands first
    if args.version:
        handle_version()
        return
    
    if args.update:
        success = handle_update_command()
        sys.exit(0 if success else 1)
    
    if args.list_providers:
        handle_list_providers()
        return
    
    if args.list_models:
        handle_list_models(args.list_models)
        return
    
    if args.status:
        handle_status()
        return
    
    # Handle interactive interface
    if args.interface:
        handle_interactive_interface()
        return
    
    # Handle editor input
    if args.editor:
        args.prompt = handle_editor_input()
    
    # Check for stdin input if no prompt provided
    if not args.prompt and not sys.stdin.isatty():
        try:
            stdin_content = sys.stdin.read().strip()
            if stdin_content:
                args.prompt = stdin_content
        except Exception as e:
            print_error(f"Error reading from stdin: {e}")
            sys.exit(1)
    # If both prompt and stdin content are available, combine them
    elif args.prompt and not sys.stdin.isatty():
        try:
            stdin_content = sys.stdin.read().strip()
            if stdin_content:
                args.prompt = f"{args.prompt}\n\nInput data:\n{stdin_content}"
        except Exception as e:
            print_error(f"Error reading from stdin: {e}")
            sys.exit(1)
    
    # Handle regular query
    handle_query(args)


if __name__ == "__main__":
    main()
