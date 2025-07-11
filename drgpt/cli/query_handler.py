"""
Query handling for DrGPT CLI

Handles AI query processing and response management.
"""

import sys
import argparse
from typing import List

from rich.markdown import Markdown

from ..core.manager import manager
from ..modes import StandardMode, CodeMode, ShellMode, ChatMode
from ..utils.console import console, print_error, print_markdown
from ..utils.file_handler import save_response_to_file
from ..utils.validation import validate_temperature, validate_max_tokens


def handle_query(args: argparse.Namespace) -> None:
    """Handle a query to the AI
    
    Args:
        args: Parsed command line arguments
    """
    if not args.prompt:
        print_error("No prompt provided")
        console.print("Use 'drgpt --help' for usage information")
        sys.exit(1)
    
    # Set provider if specified
    if args.provider or args.api_key:
        manager.set_provider(
            provider=args.provider or manager.config.get("DEFAULT_PROVIDER"),
            model=args.model,
            api_key=args.api_key
        )
    
    # Validate parameters
    try:
        temperature = validate_temperature(args.temperature)
        max_tokens = validate_max_tokens(args.max_tokens)
    except ValueError as e:
        print_error(str(e))
        sys.exit(1)
    
    # Determine mode and create mode instance
    mode = _get_mode_instance(args)
    
    # Prepare kwargs
    kwargs = {}
    if temperature is not None:
        kwargs["temperature"] = temperature
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens
    
    # Process prompt through mode
    processed_prompt = mode.process_prompt(args.prompt)
    
    # Generate response
    response_chunks = []
    try:
        if args.no_streaming:
            response_chunks = _handle_non_streaming_query(processed_prompt, args, mode, **kwargs)
        else:
            response_chunks = _handle_streaming_query(processed_prompt, args, mode, **kwargs)
            
    except KeyboardInterrupt:
        console.print("\n[[yellow]-[/yellow]] Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(str(e))
        sys.exit(1)
    
    # Save to file if requested
    if args.output:
        # Determine if we're in code or shell mode
        is_code_mode = args.code if hasattr(args, 'code') else False
        is_shell_mode = args.shell if hasattr(args, 'shell') else False
        save_response_to_file(response_chunks, args.output, is_code_mode, is_shell_mode)


def _get_mode_instance(args: argparse.Namespace):
    """Get the appropriate mode instance
    
    Args:
        args: Parsed command line arguments
        
    Returns:
        Mode instance
    """
    if args.code:
        return CodeMode(manager)
    elif args.shell:
        return ShellMode(manager)
    elif args.chat:
        return ChatMode(manager, args.chat)
    else:
        return StandardMode(manager)


def _handle_non_streaming_query(prompt: str, args: argparse.Namespace, mode, **kwargs) -> List[str]:
    """Handle non-streaming query
    
    Args:
        prompt: The processed prompt
        args: Command line arguments
        mode: The mode instance
        **kwargs: Additional query parameters
        
    Returns:
        List of response chunks
    """
    response_chunks = []
    
    with console.status("[bold green]Generating response...", spinner="dots"):
        for chunk in manager.query(
            prompt=prompt,
            provider=args.provider,
            model=args.model,
            mode=mode.get_mode_name(),
            **kwargs
        ):
            response_chunks.append(chunk)
    
    # Get the complete response and render it
    full_response = "".join(response_chunks)
    if full_response.strip():
        
        # Handle mode-specific response processing
        if isinstance(mode, ShellMode):
            mode.handle_response(full_response)
        elif args.no_markdown:
            console.print(full_response)
        else:
            # Show only markdown formatting by default for all modes
            print_markdown(full_response)
    
    return response_chunks


def _handle_streaming_query(prompt: str, args: argparse.Namespace, mode, **kwargs) -> List[str]:
    """Handle streaming query
    
    Args:
        prompt: The processed prompt
        args: Command line arguments
        mode: The mode instance
        **kwargs: Additional query parameters
        
    Returns:
        List of response chunks
    """
    response_chunks = []
    
    # Streaming mode - show response as it comes
    
    for chunk in manager.query(
        prompt=prompt,
        provider=args.provider,
        model=args.model,
        mode=mode.get_mode_name(),
        **kwargs
    ):
        if args.no_markdown:
            # Show raw text immediately if markdown is disabled
            console.print(chunk, end="")
        response_chunks.append(chunk)
    
    # Add final newline after streaming
    console.print()
    
    # Special post-processing for modes
    full_response = "".join(response_chunks)
    if isinstance(mode, ShellMode):
        mode.handle_response(full_response)
    elif not args.no_markdown:
        # Show formatted markdown version only if markdown is enabled
        if full_response.strip():
            print_markdown(full_response)
    
    return response_chunks
