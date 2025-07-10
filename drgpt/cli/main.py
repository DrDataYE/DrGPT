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


def main() -> None:
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle special commands first
    if args.version:
        handle_version()
        return
    
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
    
    # Handle regular query
    handle_query(args)


if __name__ == "__main__":
    main()
