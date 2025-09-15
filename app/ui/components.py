from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout

console = Console()


# Luo layout
layout = Layout()

# Jaa pystysuunnassa kahteen osaan
layout.split_column(
    Layout(name="header"),  # Header
    Layout(name="main"),    # Main content
)

# Jaa alaosa vaakasuunnassa kahteen osaan
layout["main"].split_row(
    Layout(name="stocks"),  # Vasen
    Layout(name="portfolio"),  # Oikea
)

# Lisää sisältöä
layout["header"].update(Panel("Trading Game", style="bold blue"))
layout["stocks"].update(Panel("Stocks", style="green"))
layout["portfolio"].update(Panel("Portfolio", style="yellow"))

# Näytä layout
console.print(layout)