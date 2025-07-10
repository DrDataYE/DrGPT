"""
Interactive interface for DrGPT CLI

Provides the interactive chat interface functionality.
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from ..core.manager import manager
from .commands import handle_status, handle_list_providers

# Initialize rich console
console = Console()


def handle_interactive_interface() -> None:
    """Handle --interface option for interactive AI chat"""
    console.print(Panel(
        "[bold green]DrGPT Interactive Interface[/bold green]\n"
        "• Type your questions after the [cyan]![/cyan] prompt\n"
        "• Type [red]exit[/red], [red]quit[/red], or press [red]Ctrl+C[/red] to exit\n"
        "• Use [yellow]!help[/yellow] for more commands",
        title="Welcome",
        border_style="green"
    ))
    
    try:
        while True:
            try:
                user_input = Prompt.ask("[bold cyan][/bold cyan]").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    console.print("[[bold green]+[/bold green]] Goodbye!")
                    break
                
                if user_input.lower() == 'help':
                    _show_help()
                    continue
                
                if user_input.lower() == 'status':
                    handle_status()
                    continue
                
                if user_input.lower() == 'providers':
                    handle_list_providers()
                    continue
                
                if user_input.lower() == 'clear':
                    console.clear()
                    continue
                
                # Handle special modes
                mode = "default"
                prompt = user_input
                
                if user_input.lower().startswith('code:'):
                    mode = "code"
                    prompt = user_input[5:].strip()
                elif user_input.lower().startswith('shell:'):
                    mode = "shell"
                    prompt = user_input[6:].strip()
                
                if not prompt:
                    console.print("{[yellow][/yellow]] Please provide a prompt after the mode.")
                    continue
                
                # Process the query
                _process_interactive_query(prompt, mode)
                
            except KeyboardInterrupt:
                console.print("\n[[yellow]-[/yellow]] Use 'exit' to quit or continue with another question.")
                continue
            except Exception as e:
                console.print(f"[[bold red]-[/bold red]] {e}")
                continue
                
    except KeyboardInterrupt:
        console.print("\n[[yellow]-[/yellow]] Goodbye!")


def _show_help() -> None:
    """Show help information for interactive interface"""
    console.print(Panel(
        "[bold]Available Commands:[/bold]\n"
        "• [cyan]help[/cyan] - Show this help\n"
        "• [cyan]status[/cyan] - Show current configuration\n"
        "• [cyan]providers[/cyan] - List available providers\n"
        "• [cyan]clear[/cyan] - Clear screen\n"
        "• [cyan]exit/quit[/cyan] - Exit interface\n\n"
        "[bold]Special Modes:[/bold]\n"
        "• Start with [yellow]code:[/yellow] for code-only responses\n"
        "• Start with [yellow]shell:[/yellow] for shell commands",
        title="Help",
        border_style="blue"
    ))


def _process_interactive_query(prompt: str, mode: str) -> None:
    """Process a query in interactive mode
    
    Args:
        prompt: The user prompt
        mode: The processing mode
    """
    from rich.markdown import Markdown
    
    
    response_chunks = []
    for chunk in manager.query(prompt=prompt, mode=mode):
        response_chunks.append(chunk)
    
    # Show formatted markdown response for all modes except shell
    full_response = "".join(response_chunks).strip()
    if full_response and mode != "shell":
        markdown = Markdown(full_response)
        console.print(markdown)
    
    # Handle special processing for shell mode
    if mode == "shell":
        from ..modes.shell import handle_shell_command
        # Extract command from response (simple heuristic)
        lines = full_response.split('\n')
        for line in lines:
            line = line.strip()
            if (line and not line.startswith('#') and 
                not line.startswith('*') and 
                not line.startswith('-') and
                ('sudo' in line or 'apt' in line or 'git' in line or 
                 'npm' in line or 'pip' in line or 'docker' in line or
                 line.startswith('cd ') or line.startswith('ls ') or
                 line.startswith('mkdir ') or line.startswith('rm '))):
                handle_shell_command(line)
                break
    
    console.print()  # Extra spacing
