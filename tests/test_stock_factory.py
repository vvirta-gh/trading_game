from app.models.stock import Stock
from app.utils.constants import GameConstants, Emojis   
from app.factories.stock_factory import StockFactory
from loguru import logger


def test_stock_factory():
    stock_factory = StockFactory()
    stocks = stock_factory.create_stocks()

    assert isinstance(stocks, list)
    assert len(stocks) == len(GameConstants.STOCK_SYMBOLS)
    assert all(isinstance(stock, Stock) for stock in stocks)
   
    logger.info(f"{Emojis.SUCCESS} Stock factory test passed! There are {len(stocks)} stocks in the list.")