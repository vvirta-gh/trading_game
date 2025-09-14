"""
Constants for the trading game application.
Contains emojis and other game constants.
"""

class Emojis:
    """Emoji constants for the trading game UI"""
    
    # Game & UI
    GAME = '🎮'
    TARGET = '🎯'
    DICE = '🎲'
    TROPHY = '🏆'
    PARTY = '🎉'
    
    # Money & Finance
    MONEY = '💰'
    DOLLAR = '💵'
    BANK = '🏦'
    CHART_UP = '📈'
    CHART_DOWN = '📉'
    DIAMOND = '💎'
    COINS = '🪙'
    
    # Status & Feedback
    SUCCESS = '✅'
    ERROR = '❌'
    WARNING = '⚠️'
    INFO = 'ℹ️'
    CHECKMARK = '✔️'
    CROSS = '❌'
    
    # Actions & Navigation
    SEARCH = '🔍'
    LIST = '📋'
    SETTINGS = '⚙️'
    BALANCE = '💳'
    PORTFOLIO = '📊'
    LEADERBOARD = '🏆'
    EXIT = '🚪'
    
    # Stock Market
    STOCK = '📈'
    TRADING = '💹'
    PROFIT = '💚'
    LOSS = '💔'
    NEUTRAL = '➡️'


class GameConstants:
    """Game configuration constants"""
    
    # Game settings
    DEFAULT_BALANCE = 1000.0
    MAX_ROUNDS = 10
    MIN_STOCK_PRICE = 24
    MAX_STOCK_PRICE = 130
    MIN_SHARES = 500
    MAX_SHARES = 10000
    
    # Stock symbols
    STOCK_SYMBOLS = [
        {"name": "Tesla Inc.", "symbol": "TSLA"},
        {"name": "Apple Inc.", "symbol": "AAPL"},
        {"name": "Nokia Oyj", "symbol": "NOK"},
        {"name": "Fortum Oyj", "symbol": "FORTUM"},
        {"name": "Neste Oyj", "symbol": "NESTE"},
    ]
