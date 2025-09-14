from app.models.stock import Stock
from app.models.player import Player
import random
from loguru import logger
from app.utils.constants import Emojis

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

    

    def run_game(self):
        """Pääpelisilmukka"""
        self._create_stocks()
        self._create_player()
        self.show_main_menu()


    def show_main_menu(self):
        """Näytä päävalikko Rich-kirjastolla tyyliteltynä"""
        from rich.console import Console
        from rich.panel import Panel
        from rich.prompt import Prompt
        
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


def run_game():
    """Entry point for demo-game script"""
    game = Game()
    game.run_game()

if __name__ == "__main__":
    game = Game()
    game.run_game()
  