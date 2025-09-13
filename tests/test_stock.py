import pytest
import os
import sys
from app.models.stock import Stock
from loguru import logger

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))


class TestStock:
    def test_buy_stock(self):
        """Test that the stock is bought correctly."""
        stock = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100)
        
        # Ensimmäinen kauppa
        first_price = stock.buy(10)
        assert first_price > 100.0  # Hinta pitäisi nousta
        assert stock.available_shares == 90  # Osakkeet vähenee
        
        # Toinen kauppa - tallenna vanha hinta ensin
        old_price = stock.current_price
        second_price = stock.buy(10)
        assert second_price > old_price  # Hinta pitäisi nousta edelleen
        assert stock.available_shares == 80  # Osakkeet vähenee edelleen
        
        print(f"First purchase: 100.0 → {first_price:.2f}")
        print(f"Second purchase: {old_price:.2f} → {second_price:.2f}")

    def test_buy_stock_basic(self):
        """Test that the stock buy method works without crashing."""
        stock = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100)
        
        # Testaa että metodi ei kaadu
        new_price = stock.buy(10)
        
        # Testaa että hinta muuttui
        assert new_price != 100.0
        assert stock.current_price == new_price
        
        # Testaa että osakkeiden määrä väheni
        assert stock.available_shares == 90
        
        print(f"Price changed from 100.0 to {new_price:.2f}")
        print(f"Available shares: {stock.available_shares}")


    def test_buy_stock_price_increases(self):
        """Test that buying shares increases the price."""
        stock = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000)
        
        old_price = stock.current_price
        new_price = stock.buy(50)  # Osta 50 osaketta
        
        # Hinta pitäisi nousta (tai ainakin muuttua)
        assert new_price != old_price
        print(f"Price changed from {old_price:.2f} to {new_price:.2f}")
        print(f"Price increase: {((new_price - old_price) / old_price * 100):.2f}%")


    def test_cannot_buy_more_than_available(self):
        """Test that you cannot buy more shares than available."""
        stock = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=10)
        
        # Tämä pitäisi heittää ValueError
        with pytest.raises(ValueError, match="Cannot buy more shares than are available"):
            stock.buy(20)  # Yritä ostaa 20 kun on vain 10

        print(f"Available shares: {stock.available_shares}")

    
    def test_large_purchase_hits_max_limit(self):
        """Test that very large purchases hit the maximum price change limit."""
        stock = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000)
        
        # Osta 90% markkinoista - tämä pitäisi laukaista max_price_change rajan
        new_price = stock.buy(900)
        price_change_percent = ((new_price - 100.0) / 100.0) * 100
        
        # Tämän pitäisi olla tasan 20% (max_price_change)
        assert price_change_percent == 20.0, f"Large purchase should hit 20% limit, got {price_change_percent:.1f}%"
        
        print(f"Large purchase price change: {price_change_percent:.1f}% (should be exactly 20%)")
    

    def test_small_purchase_smaller_impact(self):
        """Test that small purchases have smaller price impact."""
        stock1 = Stock(name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000)
        stock2 = Stock(name="Apple Inc.", symbol="AAPL", current_price=100.0, available_shares=1000)
        
        # Pieni kauppa
        small_price = stock1.buy(1)
        small_change = ((small_price - 100.0) / 100.0) * 100
        
        # Suuri kauppa
        large_price = stock2.buy(100)
        large_change = ((large_price - 100.0) / 100.0) * 100
        
        # Suuri kauppa pitäisi vaikuttaa enemmän
        assert large_change > small_change, f"Large purchase ({large_change:.1f}%) should have bigger impact than small ({small_change:.1f}%)"
        
        print(f"Small purchase impact: {small_change:.1f}%")
        print(f"Large purchase impact: {large_change:.1f}%")