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
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

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

    def test_sell_stock(self):
        """Test that the stock is sold correctly."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

        # Ensimmäinen myynti
        first_price = stock.sell(10)
        assert first_price < 100.0  # Hinta pitäisi laskea
        assert stock.available_shares == 110  # Osakkeet kasvaa

        # Toinen myynti - tallenna vanha hinta ensin
        old_price = stock.current_price
        second_price = stock.sell(10)
        assert second_price < old_price  # Hinta pitäisi laskea edelleen
        assert stock.available_shares == 120  # Osakkeet kasvaa edelleen

        print(f"First sale: 100.0 → {first_price:.2f}")
        print(f"Second sale: {old_price:.2f} → {second_price:.2f}")

    def test_buy_and_sell_cycle(self):
        """Test buying and selling in sequence."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )

        # Osta osakkeita
        buy_price = stock.buy(50)
        assert buy_price > 100.0
        assert stock.available_shares == 950

        # Myy osakkeita
        sell_price = stock.sell(25)
        assert sell_price < buy_price  # Myynti laskee hintaa
        assert stock.available_shares == 975  # Osakkeet kasvaa takaisin

        print(f"Buy 50: 100.0 → {buy_price:.2f}")
        print(f"Sell 25: {buy_price:.2f} → {sell_price:.2f}")

    def test_buy_stock_basic(self):
        """Test that the stock buy method works without crashing."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

        # Testaa että metodi ei kaadu
        new_price = stock.buy(10)

        # Testaa että hinta muuttui
        assert new_price != 100.0
        assert stock.current_price == new_price

        # Testaa että osakkeiden määrä väheni
        assert stock.available_shares == 90

        print(f"Price changed from 100.0 to {new_price:.2f}")
        print(f"Available shares: {stock.available_shares}")

    def test_sell_stock_basic(self):
        """Test that the stock sell method works without crashing."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

        # Testaa että metodi ei kaadu
        new_price = stock.sell(10)

        # Testaa että hinta muuttui
        assert new_price != 100.0
        assert stock.current_price == new_price

        # Testaa että osakkeiden määrä kasvoi
        assert stock.available_shares == 110

        print(f"Price changed from 100.0 to {new_price:.2f}")
        print(f"Available shares: {stock.available_shares}")

    def test_cannot_buy_more_than_available(self):
        """Test that you cannot buy more shares than available."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=10
        )

        # Tämä pitäisi heittää ValueError
        with pytest.raises(
            ValueError, match="Cannot buy more shares than are available"
        ):
            stock.buy(20)  # Yritä ostaa 20 kun on vain 10

    def test_cannot_sell_zero_or_negative_shares(self):
        """Test that you cannot sell zero or negative shares."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

        # Tämä pitäisi heittää ValueError
        with pytest.raises(ValueError, match="Cannot sell zero or negative shares"):
            stock.sell(0)  # Yritä myydä 0 osaketta

        with pytest.raises(ValueError, match="Cannot sell zero or negative shares"):
            stock.sell(-5)  # Yritä myydä negatiivinen määrä

    def test_price_change_within_limits(self):
        """Test that price changes are within reasonable limits."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=100
        )

        # Testaa ostoa
        buy_price = stock.buy(10)
        buy_change_percent = ((buy_price - 100.0) / 100.0) * 100

        # Hinnanmuutos pitäisi olla positiivinen ja enintään 20%
        assert buy_change_percent > 0, "Price should increase when buying shares"
        assert buy_change_percent <= 20.0, (
            f"Buy price change {buy_change_percent:.1f}% should not exceed 20%"
        )

        # Testaa myyntiä
        sell_price = stock.sell(10)
        sell_change_percent = ((sell_price - buy_price) / buy_price) * 100

        # Hinnanmuutos pitäisi olla negatiivinen ja enintään -20%
        assert sell_change_percent < 0, "Price should decrease when selling shares"
        assert sell_change_percent >= -20.0, (
            f"Sell price change {sell_change_percent:.1f}% should not exceed -20%"
        )

        print(f"Buy price change: {buy_change_percent:.1f}% (should be ≤ 20%)")
        print(f"Sell price change: {sell_change_percent:.1f}% (should be ≥ -20%)")

    def test_getter_methods(self):
        """Test that getter methods return correct values."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )

        # Testaa getter-metodit
        assert stock.get_name() == "Tesla Inc."
        assert stock.get_symbol() == "TSLA"
        assert stock.get_price() == 100.0
        assert stock.get_available_shares() == 1000
        assert stock.get_id() is not None  # ID pitäisi olla UUID

        print(f"Name: {stock.get_name()}")
        print(f"Symbol: {stock.get_symbol()}")
        print(f"Price: {stock.get_price()}")
        print(f"Available shares: {stock.get_available_shares()}")
        print(f"ID: {stock.get_id()}")

    def test_large_purchase_hits_max_limit(self):
        """Test that very large purchases hit the maximum price change limit."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )

        # Osta 90% markkinoista - tämä pitäisi laukaista max_price_change rajan
        new_price = stock.buy(900)
        price_change_percent = ((new_price - 100.0) / 100.0) * 100

        # Tämän pitäisi olla tasan 20% (max_price_change)
        assert price_change_percent == 20.0, (
            f"Large purchase should hit 20% limit, got {price_change_percent:.1f}%"
        )

        print(
            f"Large purchase price change: {price_change_percent:.1f}% (should be exactly 20%)"
        )

    def test_large_sale_hits_max_limit(self):
        """Test that very large sales hit the maximum price change limit."""
        stock = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )

        # Myy 90% markkinoista - tämä pitäisi laukaista max_price_change rajan
        new_price = stock.sell(900)
        price_change_percent = ((new_price - 100.0) / 100.0) * 100

        # Tämän pitäisi olla tasan -20% (max_price_change)
        assert price_change_percent == -20.0, (
            f"Large sale should hit -20% limit, got {price_change_percent:.1f}%"
        )

        print(
            f"Large sale price change: {price_change_percent:.1f}% (should be exactly -20%)"
        )

    def test_small_purchase_smaller_impact(self):
        """Test that small purchases have smaller price impact."""
        stock1 = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )
        stock2 = Stock(
            name="Apple Inc.", symbol="AAPL", current_price=100.0, available_shares=1000
        )

        # Pieni kauppa
        small_price = stock1.buy(1)
        small_change = ((small_price - 100.0) / 100.0) * 100

        # Suuri kauppa
        large_price = stock2.buy(100)
        large_change = ((large_price - 100.0) / 100.0) * 100

        # Suuri kauppa pitäisi vaikuttaa enemmän
        assert large_change > small_change, (
            f"Large purchase ({large_change:.1f}%) should have bigger impact than small ({small_change:.1f}%)"
        )

        print(f"Small purchase impact: {small_change:.1f}%")
        print(f"Large purchase impact: {large_change:.1f}%")

    def test_small_sale_smaller_impact(self):
        """Test that small sales have smaller price impact."""
        stock1 = Stock(
            name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
        )
        stock2 = Stock(
            name="Apple Inc.", symbol="AAPL", current_price=100.0, available_shares=1000
        )

        # Pieni myynti
        small_price = stock1.sell(1)
        small_change = ((small_price - 100.0) / 100.0) * 100

        # Suuri myynti
        large_price = stock2.sell(100)
        large_change = ((large_price - 100.0) / 100.0) * 100

        # Suuri myynti pitäisi vaikuttaa enemmän (laskea hintaa enemmän)
        assert large_change < small_change, (
            f"Large sale ({large_change:.1f}%) should have bigger impact than small ({small_change:.1f}%)"
        )

        print(f"Small sale impact: {small_change:.1f}%")
        print(f"Large sale impact: {large_change:.1f}%")
