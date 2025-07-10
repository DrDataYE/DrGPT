"""
Update functionality for DrGPT

Handles automatic updates from PyPI and GitHub releases.
"""

import subprocess
import sys
import json
import requests
from packaging import version
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm

from .. import __version__


console = Console()


class DrGPTUpdater:
    """Handles DrGPT updates from PyPI and GitHub"""
    
    PYPI_API_URL = "https://pypi.org/pypi/drgpt/json"
    GITHUB_API_URL = "https://api.github.com/repos/DrDataYE/drgpt/releases/latest"
    
    def __init__(self):
        self.current_version = __version__
        
    def check_pypi_version(self) -> tuple[str, bool]:
        """Check latest version on PyPI
        
        Returns:
            Tuple of (latest_version, update_available)
        """
        try:
            response = requests.get(self.PYPI_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            latest_version = data["info"]["version"]
            
            update_available = version.parse(latest_version) > version.parse(self.current_version)
            return latest_version, update_available
            
        except Exception as e:
            console.print(f"[red]Error checking PyPI: {e}[/red]")
            return self.current_version, False
    
    def check_github_version(self) -> tuple[str, bool]:
        """Check latest version on GitHub releases
        
        Returns:
            Tuple of (latest_version, update_available)
        """
        try:
            response = requests.get(self.GITHUB_API_URL, timeout=10)
            response.raise_for_status()
            data = response.json()
            latest_version = data["tag_name"].lstrip("v")
            
            update_available = version.parse(latest_version) > version.parse(self.current_version)
            return latest_version, update_available
            
        except Exception as e:
            console.print(f"[red]Error checking GitHub: {e}[/red]")
            return self.current_version, False
    
    def update_from_pypi(self) -> bool:
        """Update DrGPT from PyPI
        
        Returns:
            True if update was successful
        """
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Updating from PyPI...", total=None)
                
                # Run pip install --upgrade
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", "--upgrade", "drgpt"
                ], capture_output=True, text=True, check=True)
                
                progress.update(task, completed=True)
                
            console.print("[green]✅ Successfully updated from PyPI![/green]")
            console.print("[yellow]Please restart your terminal to use the new version.[/yellow]")
            return True
            
        except subprocess.CalledProcessError as e:
            console.print(f"[red]❌ Update failed: {e.stderr}[/red]")
            return False
        except Exception as e:
            console.print(f"[red]❌ Update error: {e}[/red]")
            return False
    
    def update_from_github(self) -> bool:
        """Update DrGPT from GitHub source
        
        Returns:
            True if update was successful
        """
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task("Updating from GitHub...", total=None)
                
                # Run pip install from GitHub
                result = subprocess.run([
                    sys.executable, "-m", "pip", "install", "--upgrade",
                    "git+https://github.com/DrDataYE/drgpt.git"
                ], capture_output=True, text=True, check=True)
                
                progress.update(task, completed=True)
                
            console.print("[green]✅ Successfully updated from GitHub![/green]")
            console.print("[yellow]Please restart your terminal to use the new version.[/yellow]")
            return True
            
        except subprocess.CalledProcessError as e:
            console.print(f"[red]❌ Update failed: {e.stderr}[/red]")
            return False
        except Exception as e:
            console.print(f"[red]❌ Update error: {e}[/red]")
            return False
    
    def show_update_info(self, pypi_version: str, github_version: str, 
                        pypi_available: bool, github_available: bool):
        """Show update information to user"""
        
        info_lines = [
            f"Current Version: [cyan]{self.current_version}[/cyan]",
            f"PyPI Latest: [green]{pypi_version}[/green]" + (" ✨ (Update available)" if pypi_available else ""),
            f"GitHub Latest: [green]{github_version}[/green]" + (" ✨ (Update available)" if github_available else ""),
        ]
        
        panel = Panel(
            "\n".join(info_lines),
            title="[bold]DrGPT Version Information[/bold]",
            border_style="blue"
        )
        console.print(panel)
    
    def update(self, force: bool = False, source: str = "auto") -> bool:
        """Main update function
        
        Args:
            force: Force update even if no newer version is found
            source: Update source ("pypi", "github", or "auto")
            
        Returns:
            True if update was performed
        """
        console.print("[bold]🔄 Checking for DrGPT updates...[/bold]")
        
        # Check versions
        pypi_version, pypi_available = self.check_pypi_version()
        github_version, github_available = self.check_github_version()
        
        # Show current status
        self.show_update_info(pypi_version, github_version, pypi_available, github_available)
        
        # Determine if update is needed
        if not force and not pypi_available and not github_available:
            console.print("[green]✅ You are already running the latest version![/green]")
            return False
        
        # Determine update source
        if source == "auto":
            if pypi_available:
                source = "pypi"
            elif github_available:
                source = "github"
            else:
                source = "github"  # Default fallback
        
        # Confirm update
        if source == "pypi":
            update_msg = f"Update from PyPI v{self.current_version} → v{pypi_version}?"
        else:
            update_msg = f"Update from GitHub v{self.current_version} → v{github_version}?"
            
        if not force and not Confirm.ask(update_msg):
            console.print("[yellow]Update cancelled.[/yellow]")
            return False
        
        # Perform update
        if source == "pypi":
            return self.update_from_pypi()
        else:
            return self.update_from_github()


def handle_update_command(force: bool = False, source: str = "auto") -> bool:
    """Handle the --update command
    
    Args:
        force: Force update even if no newer version is found
        source: Update source preference
        
    Returns:
        True if update was successful
    """
    updater = DrGPTUpdater()
    return updater.update(force=force, source=source)
