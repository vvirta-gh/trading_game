import time
from loguru import logger
from app.ui.layout import GameLayout
from app.ui.components import UIComponents
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


class GameInterface:
    def __init__(self):
        self.layout = GameLayout()
        self.components = UIComponents()
        self.current_day = 0

    def show_game_interface(self, player, stocks):
        console = Console()
        
        # Tervetuloa
        welcome_text = f"[bold blue]Welcome {player.name}![/bold blue]\n[italic]The market awaits your strategy...[/italic]"
        console.print(Panel(welcome_text, title="🎮 Trading Game", border_style="blue"))
        
        # Shark/Fish valinta
        strategy_text = """
[bold yellow]What's your trading style?[/bold yellow]
[green] Shark:[/green] Aggressive, quick profits, high risk
[blue]🐟 Fish:[/blue] Conservative, steady gains, low risk
"""
        console.print(Panel(strategy_text, title="Choose Your Strategy", border_style="yellow"))
        
        choice = input("Are you a shark or fish? (s/f): ").lower()
        if choice == 's':
            player.strategy = "shark"
            console.print("[bold red]🦈 SHARK MODE ACTIVATED![/bold red]")
        else:
            player.strategy = "fish" 
            console.print("[bold blue]🐟 FISH MODE ACTIVATED![/bold blue]")
        
        time.sleep(2)
        
        # Päivä
        day_text = f"[bold green]Day {self.current_day + 1} starting soon...[/bold green]"
        console.print(Panel(day_text, title="📈 Market Opening", border_style="green"))
        time.sleep(2)
        
        # Aseta osakkeet komponenteille
        self.components.set_stocks(stocks)
        
        # Luo sisältö
        stocks_table = self.components.create_stocks_table()
        portfolio_table = self.components.create_portfolio_table()
        
        # Täytä layout
        self.layout.update_header(f"Day {self.current_day + 1} starting...")
        self.layout.update_stocks(stocks_table)
        self.layout.update_portfolio(portfolio_table)
        self.layout.update_actions()
        self.layout.update_status()
        
        # Renderöi
        self.layout.render()
        

        return "exit"