from app.models.stock import Stock
from app.models.player import Player
import random
from loguru import logger


class Game:
    """Game class handles game logic and flow"""
    def __init__(self, player_name: str = "Trader"):
        self.player = Player(player_name, balance=1000.0)   # 1000€ aloitusrahaa
        self.stocks = []    # 5 osaketta
        self.current_round = 1
        self.max_rounds = 10
        self.leaderboard = []   # tallentaa pelitulokset statistiikaksi
   

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


if __name__ == "__main__":
    game = Game()
    game._create_stocks()