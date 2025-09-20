from app.models.stock import Stock
from app.models.player import Player
from app.utils.constants import Emojis
from app.ui.game_interface import GameInterface

import random
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


class Game:
    """
    Game class handles game logic and flow
    """

    def __init__(self):
        self.player = None
        self.stocks = []    # 5 osaketta
        self.current_round = 1
        self.max_rounds = 10
        self.leaderboard = []   # tallentaa pelitulokset statistiikaksi
        self.console = Console()
        self.game_interface = GameInterface()

    def run_game(self):
        """Pääpelisilmukka"""
        self._create_stocks()

        menu_actions = {
            "1": self.start_new_game,
            "2": self.show_portfolio,
            "3": self.show_leaderboard,
            "4": self.show_settings,
            "5": self.exit_game
        }

        while True:
            choice = self.show_main_menu()

            action = menu_actions.get(choice)
            if action:
                result = action()
                if result == "exit":
                    break
            else:
                self.console.print(
                    f"[red bold]{Emojis.ERROR} Invalid choice!n[/red bold]")

    def show_main_menu(self):
        """Näytä päävalikko Rich-kirjastolla tyyliteltynä"""

        console = Console()

        menu_text = (
            f"[bold blue]{Emojis.CHART_UP} Trading Game {Emojis.CHART_DOWN}[/bold blue]\n"
            "Choose an option:\n"
            "1. Start Game\n"
            "2. Show Portfolio\n"
            "3. Show Leaderboard\n"
            "4. Settings\n"
            "5. Exit"
        )

        console.print(Panel.fit(menu_text, title="Main Menu"))

        choice = Prompt.ask(
            "Choose an option:",
            choices=["1", "2", "3", "4", "5"],
            default="1",
        )

        return choice

    def _create_stocks(self):
        stocks_data = [
            {"name": "Tesla Inc.", "symbol": "TSLA"},
            {"name": "Apple Inc.", "symbol": "AAPL"},
            {"name": "Nokia Oyj", "symbol": "NOK"},
            {"name": "Fortum Oyj", "symbol": "FORTUM"},
            {"name": "Neste Oyj", "symbol": "NESTE"},
        ]

        for stock_data in stocks_data:
            logger.debug(f"Creating stock: {stock_data}")
            stock = Stock(
                name=stock_data["name"],
                symbol=stock_data["symbol"],
                current_price=random.randint(24, 130),
                available_shares=random.randint(500, 10000)
            )
            self.stocks.append(stock)
        logger.debug(f"Created {len(self.stocks)} stocks")

    def _create_player(self, player_name: str = "Trader"):
        self.player = Player(name=player_name, balance=1000.0)
        logger.debug(f"Created player: {self.player.get_name()}")
        return self.player

    def start_new_game(self):
        """Aloita uusi peli"""
        player_name = Prompt.ask("Enter your name: ", default="Trader Joe")
        self._create_player(player_name)
        self.console.print(f"Welcome {player_name}! Let's start the game!")
        
        # Käynnistä pelin käyttöliittymä
        result = self.game_interface.show_game_interface(self.player, self.stocks)
        if result == "exit":
            return

    def play_trading_rounds(self):
        self.console.print(f"Playing {self.max_rounds} trading rounds")
        self.console.print(f"Stocks: {self.stocks}")
        self.console.print(f"Balance: {self.player.balance}")

    def show_portfolio(self):  # ✅ Oikea indentointi
        """Näytä portfolio"""
        pass

    def show_leaderboard(self):  # ✅ Oikea indentointi
        """Näytä leaderboard"""
        pass

    def show_settings(self):
        """Näytä asetukset"""
        pass

    def exit_game(self):  # ✅ Oikea indentointi
        """Lopeta peli"""
        return "exit"


def run_game():
    """Entry point for demo-game script"""
    game = Game()
    game.run_game()


if __name__ == "__main__":
    game = Game()
    game.run_game()
