"""
Shell mode for DrGPT

Handles shell command generation and execution.
"""

import subprocess
from rich.console import Console
from rich.prompt import Prompt, Confirm

from .base import BaseMode

# Initialize rich console
console = Console()


class ShellMode(BaseMode):
    """Shell command mode for DrGPT"""
    
    def process_prompt(self, prompt: str, **kwargs) -> str:
        """Process prompt for shell mode
        
        Args:
            prompt: The user prompt
            **kwargs: Additional arguments
            
        Returns:
            Modified prompt for shell command generation
        """
        return f"""Generate a single shell command for the following request. 

Request: {prompt}

Rules:
- Return ONLY the shell command, no explanations
- Use Linux/Unix commands unless Windows is specifically mentioned
- Make the command safe and practical
- If multiple steps are needed, combine with && or ;
- Do not include any markdown formatting

Command:"""
    
    def handle_response(self, response: str, **kwargs) -> None:
        """Handle shell command response
        
        Args:
            response: The AI response containing shell command
            **kwargs: Additional arguments
        """
        # Extract command from response
        command = self._extract_command(response)
        if command:
            handle_shell_command(command)
        else:
            console.print("[[yellow]![/yellow]] No valid command found in response.")
            console.print("\n[dim]Full AI response:[/dim]")
            console.print(response)
            console.print("\n[dim]Please try rephrasing your request or use a more specific prompt.[/dim]")
    
    def _extract_command(self, response: str) -> str:
        """Extract shell command from AI response
        
        Args:
            response: The AI response
            
        Returns:
            Extracted command or empty string
        """
        # Remove any markdown formatting and extract the actual command
        lines = response.strip().split('\n')
        command_lines = []
        
        for line in lines:
            line = line.strip()
            # Skip empty lines, comments, and markdown
            if not line or line.startswith('#') or line.startswith('*') or line.startswith('-'):
                continue
            # Skip markdown code block markers
            if line.startswith('```') or line.endswith('```'):
                continue
            # Remove backticks if present
            if line.startswith('`') and line.endswith('`'):
                line = line[1:-1].strip()
            
            # If we found a command line, add it
            if line:
                command_lines.append(line)
        
        # Return the first valid command line, or join multiple if they're continuation
        if command_lines:
            # Handle multi-line commands (ending with \)
            full_command = ""
            for cmd in command_lines:
                if full_command:
                    full_command += " " + cmd
                else:
                    full_command = cmd
                # If it doesn't end with continuation, break
                if not cmd.endswith('\\'):
                    break
            return full_command
        
        return ""


def handle_shell_command(command: str) -> None:
    """Handle shell command with interactive options
    
    Args:
        command: The shell command to handle
    """
    # Display the generated command
    console.print(command, style="dim")
    
    while True:
        choice = console.input(
            "\n[bold white][E]xecute, [D]escribe, [A]bort: [/bold white]",
        ).lower().strip()
        
        if choice in ['a', 'abort']:
            console.print("[[bold green]+[/bold green]] Command aborted.")
            break
        elif choice in ['e', 'execute']:
            _execute_command(command)
            break
        elif choice in ['d', 'describe']:
            _describe_command(command)
        else:
            console.print("[[yellow]![/yellow]] Please enter 'e' (execute), 'd' (describe), or 'a' (abort)")
            continue


def _execute_command(command: str) -> None:
    """Execute a shell command with user confirmation
    
    Args:
        command: The shell command to execute
    """
    try:
        console.print("\n[dim]Executing command...[/dim]")
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.stdout:
            console.print("[[bold green]+[/bold green]] Output:")
            console.print(result.stdout)
        
        if result.stderr:
            console.print("[[bold red]-[/bold red]] Error:")
            console.print(result.stderr)
        
        console.print(f"\n[dim]Exit code: {result.returncode}[/dim]")
        
    except subprocess.TimeoutExpired:
        console.print("[[bold red]-[/bold red]] Command timed out (5 minutes)")
    except Exception as e:
            console.print(f"[[bold red]-[/bold red]] Error executing command: {e}")



def _describe_command(command: str) -> None:
    """Get AI description of a shell command
    
    Args:
        command: The shell command to describe
    """
    from rich.markdown import Markdown
    from ..core.manager import manager
    
    console.print("\n[dim]Getting command description...[/dim]")
    try:
        description_chunks = []
        for chunk in manager.query(
            prompt=f"Explain this shell command in detail: {command}",
            mode="default"
        ):
            description_chunks.append(chunk)
        
        description = "".join(description_chunks)
        if description.strip():
            markdown = Markdown(description)
            console.print(markdown)
        
    except Exception as e:
        console.print(f"[[bold red]-[/bold red]] Error getting description: {e}")
