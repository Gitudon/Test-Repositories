from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Top Movies 2025")
table.add_column("Rank", justify="right", style="cyan")
table.add_column("Title", style="magenta")
table.add_column("Rating", justify="right", style="green")

table.add_row("1", "Inception 2", "9.5")
table.add_row("2", "The Matrix Resurrections", "9.0")
table.add_row("3", "Interstellar: The Return", "8.8")
console.print(table)
