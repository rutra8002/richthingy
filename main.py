from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
import os
import time

console = Console()

class Player:
    def __init__(self, name):
        self.name = name

def play_game():
    """Placeholder for game functionality"""
    player_name = console.input("[b]Enter your name:[/b] ")
    player = Player(player_name)
    console.print(Panel(f"Hello, {player.name}! Game functionality would go here", title="Play"))
    turns = 0
    while True:
        turns += 1
        console.print(Panel(f"Turn {turns}", title="Game Turn"))
        console.print("Game actions would happen here...")

        console.print("\n[b]Options:[/b]")
        console.print("1: Submit")
        console.print("d: Read Documentation")
        console.print("q: Quit to Main Menu")

        choice = console.input("\n[b]Enter your choice:[/b] ")

        if choice == "1":
            console.print("Continuing game...")
            time.sleep(1)
        elif choice == "d":
            read_documentation()
        elif choice == "q":
            console.print("Quitting to Main Menu...")
            break
        else:
            console.print(Panel("Invalid choice. Please try again.", style="bold red"))
            console.input("\n[i]Press Enter to continue...[/i]")

    console.input("\n[i]Press Enter to return to the main menu...[/i]")


def read_documentation():
    """Read and display README file content"""
    try:
        readme_path = "README.md"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as file:
                content = file.read()
            markdown = Markdown(content)
            console.print(Panel(markdown, title="Documentation"))
        else:
            console.print(Panel("README.md file not found", title="Error", style="bold red"))
    except Exception as e:
        console.print(Panel(f"Error: {str(e)}", title="Error", style="bold red"))

    console.input("\n[i]Press Enter to continue...[/i]")


def main_menu():
    """Display main menu and handle user choices"""
    while True:
        console.clear()
        console.print(Panel("Main Menu", title="Application"))

        options = [
            "[1] Play",
            "[2] Read Documentation",
            "[3] Quit"
        ]

        for option in options:
            console.print(option)

        choice = console.input("\n[b]Enter your choice (1-3):[/b] ")

        if choice == "1":
            play_game()
        elif choice == "2":
            read_documentation()
        elif choice == "3":
            console.print(Panel("Goodbye!", title="Exiting"))
            break
        else:
            console.print(Panel("Invalid choice. Please try again.", style="bold red"))
            console.input("\n[i]Press Enter to continue...[/i]")


if __name__ == "__main__":
    main_menu()