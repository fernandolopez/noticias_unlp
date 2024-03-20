from rich.console import Console
from rich.table import Table

def as_table(news):
    table = Table(title="Info UNLP news", show_lines=True)
    table.add_column("Title", justify="left", style="cyan", width=30)
    table.add_column("Content", justify="left", style="magenta")
    
    for article in news:
        table.add_row(article["title"], article["content"])

    console = Console()
    console.print(table)