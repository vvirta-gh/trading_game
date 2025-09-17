from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from app.utils.constants import Emojis


class GameInterface:
    """Pelin käyttöliittymä"""
    
    def __init__(self):
        self.console = Console()
    
    def show_game_interface(self, player, stocks):
        """Näytä pelin pääkäyttöliittymä"""
        while True:
            self._clear_screen()
            self._show_header(player)
            self._show_stocks(stocks)
            self._show_portfolio(player)
            
            choice = self._show_game_menu()
            
            if choice == "1":
                self._buy_stock(player, stocks)
            elif choice == "2":
                self._sell_stock(player)
            elif choice == "3":
                self._next_round()
                break
            elif choice == "4":
                return "exit"
    
    def _clear_screen(self):
        """Tyhjennä ruutu"""
        self.console.clear()
    
    def _show_header(self, player):
        """Näytä pelin header"""
        header_text = f"{Emojis.CHART_UP} Trading Game {Emojis.CHART_DOWN}"
        balance_text = f"Balance: {Emojis.MONEY} {player.balance:.2f}"
        
        self.console.print(Panel.fit(
            f"{header_text}\n{balance_text}",
            title=f"Player: {player.name}",
            style="bold blue"
        ))
    
    def _show_stocks(self, stocks):
        """Näytä osakkeet taulukkona"""
        table = Table(title="Available Stocks", style="green")
        table.add_column("Symbol", style="cyan")
        table.add_column("Name", style="white")
        table.add_column("Price", style="green")
        table.add_column("Available", style="yellow")
        
        for stock in stocks:
            table.add_row(
                stock.symbol,
                stock.name,
                f"{Emojis.MONEY} {stock.current_price:.2f}",
                str(stock.available_shares)
            )
        
        self.console.print(table)
    
    def _show_portfolio(self, player):
        """Näytä pelaajan portfolio"""
        if not player.portfolio:
            self.console.print(Panel("Portfolio is empty", style="yellow"))
            return
        
        table = Table(title="Your Portfolio", style="yellow")
        table.add_column("Symbol", style="cyan")
        table.add_column("Name", style="white")
        table.add_column("Shares", style="green")
        table.add_column("Current Price", style="green")
        table.add_column("Value", style="bold green")
        
        total_value = 0
        for stock in player.portfolio:
            # Tässä pitäisi laskea kuinka monta osaketta pelaajalla on
            # Mutta Player-luokassa ei ole tätä tietoa vielä
            table.add_row(
                stock.symbol,
                stock.name,
                "1",  # Placeholder
                f"{Emojis.MONEY} {stock.current_price:.2f}",
                f"{Emojis.MONEY} {stock.current_price:.2f}"
            )
            total_value += stock.current_price
        
        self.console.print(table)
        self.console.print(f"Total Portfolio Value: {Emojis.MONEY} {total_value:.2f}")
    
    def _show_game_menu(self):
        """Näytä pelin valikko"""
        menu_text = (
            "What would you like to do?\n"
            "1. Buy Stock\n"
            "2. Sell Stock\n"
            "3. Next Round\n"
            "4. Exit to Main Menu"
        )
        
        self.console.print(Panel.fit(menu_text, title="Game Menu"))
        
        choice = Prompt.ask(
            "Choose an option:",
            choices=["1", "2", "3", "4"],
            default="1"
        )
        
        return choice
    
    def _buy_stock(self, player, stocks):
        """Osta osaketta"""
        # TODO: Toteuta osakkeen osto
        self.console.print("[yellow]Buy stock functionality not implemented yet![/yellow]")
        input("Press Enter to continue...")
    
    def _sell_stock(self, player):
        """Myy osaketta"""
        # TODO: Toteuta osakkeen myynti
        self.console.print("[yellow]Sell stock functionality not implemented yet![/yellow]")
        input("Press Enter to continue...")
    
    def _next_round(self):
        """Siirry seuraavalle kierrokselle"""
        self.console.print("[green]Moving to next round...[/green]")
        input("Press Enter to continue...")
