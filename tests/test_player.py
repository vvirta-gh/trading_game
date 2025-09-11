import pytest
import sys
import os

# Lisätään app-kansion Python pathiin
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from app.models.player import Player

class TestPlayer:
    def test_player_init(self):
        """Test that the player is initialized correctly."""
        player = Player()

        assert player.name == "Trader"
        assert player.balance == 5000.00
        assert player.portfolio == []

  
    # def test_buy_stock(self):
    #     """Test that the player can buy a stock."""
    #     player = Player()
    #     stock = Stock(name="Tesla Inc.", "TSLA",100.0, 1)
        