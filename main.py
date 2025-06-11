from rich.panel import Panel
from rich.console import Console

console = Console()

# Simple panel
console.print(Panel("Hello, World!", title="Greeting"))

# Panel with custom styling
console.print(
    Panel(
        "This is important information!",
        title="Alert",
        style="bold red",
        border_style="red"
    )
)