from typing import List
from models.stock import Stock
from loguru import logger


class Player:
    def __init__(self, name: str = "Trader", balance: float = 5000.00):
        self.name = name
        self.balance = balance
        self.portfolio = []

    def buy_stock(self, stock: Stock, count: int):
        """Buy a stock for the  player."""
        self.balance -= stock.current_price * count
        logger.info(
            f"Player {self.name} bought {count} stocks of {stock.name} for {stock.current_price * count}."
        )
        logger.info(f"Player {self.name} has {self.balance} left in balance.")
        stock.buy(count)
        self.portfolio.append(stock)
        logger.info(f"Player {self.name} has {self.portfolio} in portfolio.")
        return self.balance, self.portfolio


if __name__ == "__main__":
    player = Player()
    print(player.name)
    print(player.balance)
    print(player.portfolio)
