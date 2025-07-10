"""
Command handlers for DrGPT CLI

Contains handlers for various CLI commands and operations.
"""

from rich.console import Console

from ..core.manager import manager
from ..core.config import SUPPORTED_PROVIDERS

# Initialize rich console
console = Console()


def handle_list_providers() -> None:
    """Handle --list-providers command"""
    console.print("\n[[bold green]+[/]] Available AI providers and models:\n")
    
    providers = manager.list_providers()
    for provider_name, models in providers.items():
        console.print(f"[bold]{provider_name}:[/bold]")
        if models:
            for model in models:
                console.print(f"  [green]•[/green] {model}")
        else:
            console.print(f"  [green]•[/green] [italic](custom models)[/italic]")
        console.print()


def handle_list_models(provider: str) -> None:
    """Handle --list-models command
    
    Args:
        provider: Provider name to list models for
    """
    if provider not in SUPPORTED_PROVIDERS:
        console.print(f"[[bold red]-[/bold red]] Unsupported provider '{provider}'")
        console.print(f"[[bold green]+[/]] Available providers: {', '.join(SUPPORTED_PROVIDERS.keys())}")
        return
    
    models = SUPPORTED_PROVIDERS[provider]["models"]
    console.print(f"\n[[bold green]+[/bold green]] Available models for {provider}:\n")
    
    if models:
        for model in models:
            console.print(f"  [green]•[/green] {model}")
    else:
        console.print(f"  [green]•[/green] [italic](custom models)[/italic]")


def handle_status() -> None:
    """Handle --status command"""
    status = manager.get_status()
    
    # Create status panel
    console.print("\nProvider: ", style="bold", end="")
    console.print(f"{status['provider']}")
    
    console.print("Model: ", style="bold", end="")
    console.print(f"{status['model']}")
    
    console.print("API Key: ", style="bold", end="")
    if status['has_api_key']:
        console.print("[bold green]✓[/bold green] Set")
    else:
        console.print("[bold red]✗[/bold red] Not set")
    
    console.print("Config: ", style="bold", end="")
    console.print(f"{status['config_path']}")
    
    console.print("Available providers: ", style="bold", end="")
    console.print(f"{', '.join(status['available_providers'])}")
    console.print()
    
   


def handle_version() -> None:
    """Handle --version command"""
    from .. import __version__, __description__
    
    console.print(f"DrGPT v{__version__}", style="bold")
    console.print(__description__, style="dim")
