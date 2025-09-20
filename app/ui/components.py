from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from app.utils.constants import Emojis, GameConstants


class UIComponents:
    """UI-komponentit pelille"""

    def __init__(self):
        self.console = Console()
        self.stocks = None
        self.portfolio = None

    def set_stocks(self, stocks):
        self.stocks = stocks

    def set_portfolio(self, portfolio):
        self.portfolio = portfolio

    def create_stocks_table(self):
        """Creates a table for the stocks"""
        if not self.stocks:
            return Table(title="No stocks available")

        table = Table(title="Available Stocks", style="green")
        table.add_column("Symbol", style="cyan")
        table.add_column("Company", style="white")
        table.add_column("Price", style="green")
        table.add_column("Available", style="yellow")
        
        for stock in self.stocks:
            table.add_row(
                stock.symbol,
                stock.name,
                f"{Emojis.MONEY} {stock.current_price:.2f}",
                str(stock.available_shares)
            )
        
        return table

    def create_portfolio_table(self):
        """Creates a table for the portfolio"""
        table = Table(title="Your Portfolio", style="cyan")
        table.add_column("Symbol", style="cyan")
        table.add_column("Shares", style="green")
        table.add_column("Price", style="green")
        table.add_column("Value", style="bold green")
        
        if not self.portfolio:
            table.add_row("Empty", "-", "-", "-")
        else:
            for stock in self.portfolio:
                table.add_row(
                    stock.symbol,
                    "1",  # Placeholder
                    f"{Emojis.MONEY} {stock.current_price:.2f}",
                    f"{Emojis.MONEY} {stock.current_price:.2f}"
                )
        
        return table


if __name__ == "__main__":
    components = UIComponents()
