
from app.utils import constants
from app.utils.constants import GameConstants
from app.models.stock import Stock
import random


class StockFactory:
    """Factory for creating stocks"""
    def __init__(self):
        self.constants = GameConstants()
    
    def create_stocks(self):
        stocks = []

        for stock_data in self.constants.STOCK_SYMBOLS:
            stock = Stock(
                name=stock_data["name"],
                symbol=stock_data["symbol"],
                current_price=random.uniform(self.constants.MIN_STOCK_PRICE, self.constants.MAX_STOCK_PRICE),
                available_shares=random.uniform(self.constants.MIN_SHARES, self.constants.MAX_SHARES)
            )
            stocks.append(stock)

        return stocks

if __name__ == "__main__":
    stock_factory = StockFactory()
    stocks = stock_factory.create_stocks()
    print(stocks)