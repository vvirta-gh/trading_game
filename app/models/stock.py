import uuid
from loguru import logger
import math
import random
from app.config.stock_config import STOCK_CONFIG


class Stock:
    def __init__(
        self, name: str, symbol: str, current_price: float, available_shares: int
    ):
        self.id = uuid.uuid4()
        self.name = name
        self.symbol = symbol
        self.current_price = current_price
        self.available_shares = available_shares

    def buy(self, shares_to_buy: int):
        """
        Simuloi osakkeen ostamista ja laskee uuden hinnan markkinoiden tarjonta-kysyntä mallin mukaan.

        Hinta lasketaan neljän tekijän perusteella:
        1. Markkinoiden vaikutus - kuinka suuri osa markkinoista ostetaan
        2. Tarjonta-kysyntä - kuinka harvinaisia osakkeet ovat
        3. Logaritminen kasvu - estää liian jyrkät hinnankorotukset
        4. Satunnainen volatiliteetti - tekee pelistä mielenkiintoisen
        """
        if shares_to_buy > self.available_shares:
            raise ValueError("Cannot buy more shares than are available.")

        # Hae konfiguraatioarvot
        weights = STOCK_CONFIG["price_change_weights"]
        market_sensitivity = STOCK_CONFIG["market_sensitivity"]
        volatility_range = STOCK_CONFIG["volatility_range"]
        max_price_change = STOCK_CONFIG["max_price_change"]
        normal_supply = STOCK_CONFIG["normal_supply"]

        # 1. MARKKINOIDEN VAIKUTUS
        # Laske kuinka suuri osa markkinoista ostetaan kerralla
        # Esim: jos on 1000 osaketta ja ostat 100, niin market_impact = 0.1 (10%)
        market_impact = shares_to_buy / self.available_shares
        logger.info(
            f"Market impact: {market_impact:.3f} ({market_impact * 100:.1f}% of market)"
        )

        # 2. TARJONTA-KYSYNTÄ TEKIJÄ
        # Mitä vähemmän osakkeita on jäljellä, sitä korkeampi hinta
        # Esim: jos on 50 osaketta jäljellä (normaali=100), scarcity_factor = 2.0
        scarcity_factor = normal_supply / self.available_shares
        logger.info(
            f"Scarcity factor: {scarcity_factor:.3f} (normal supply: {normal_supply})"
        )

        # 3. LOGARITMINEN KASVU
        # Estää liian jyrkät hinnankorotukset suurilla kaupoilla
        # Esim: 10 osaketta -> log(1 + 10*0.05) = log(1.5) ≈ 0.405
        log_factor = math.log(1 + shares_to_buy * market_sensitivity)
        logger.info(
            f"Log factor: {log_factor:.3f} (shares: {shares_to_buy}, sensitivity: {market_sensitivity})"
        )

        # 4. SATUNNAINEN VOLATILITEETTI
        # Lisää arvaamattomuutta peliin
        # Esim: random.uniform(-0.01, 0.01) antaa arvon välillä -1% ja +1%
        volatility = random.uniform(-volatility_range, volatility_range)
        logger.info(f"Volatility: {volatility:.3f} ({volatility * 100:.1f}%)")

        # YHDISTÄ KAIKKI TEKIJÄT
        # Kukin tekijä kerrotaan painokertoimella ja lasketaan yhteen
        total_change = (
            market_impact * weights["market_impact"]
            + scarcity_factor * weights["scarcity_factor"]
            + log_factor * weights["log_factor"]
            + volatility * weights["volatility"]
        )

        # RAJOITA MUUTOS JÄRKEVÄÄN RAJAAN
        # Estää liian jyrkät hinnanmuutokset (esim. max 20%)
        total_change = min(total_change, max_price_change)
        logger.info(
            f"Total price change: {total_change:.3f} ({total_change * 100:.1f}%)"
        )

        # PÄIVITÄ HINTA
        old_price = self.current_price
        self.current_price *= 1 + total_change
        self.available_shares -= shares_to_buy

        logger.info(f"Price changed from {old_price:.2f} to {self.current_price:.2f}")
        logger.info(f"Available shares: {self.available_shares}")

        return self.current_price

    def sell(self, shares_to_sell: int):
        """
        Simuloi osakkeen myyntiä ja laskee uuden hinnan markkinoiden tarjonta-kysyntä mallin mukaan.

        Myynti toimii käänteisesti ostamiseen:
        - Hinta laskee kun myydään osakkeita
        - Mitä enemmän myydään, sitä enemmän hinta laskee
        - Tarjonta kasvaa (available_shares kasvaa)
        """
        if shares_to_sell <= 0:
            raise ValueError("Cannot sell zero or negative shares.")

        # Hae konfiguraatioarvot
        weights = STOCK_CONFIG["price_change_weights"]
        market_sensitivity = STOCK_CONFIG["market_sensitivity"]
        volatility_range = STOCK_CONFIG["volatility_range"]
        max_price_change = STOCK_CONFIG["max_price_change"]
        normal_supply = STOCK_CONFIG["normal_supply"]

        # 1. MARKKINOIDEN VAIKUTUS (käänteinen)
        # Laske kuinka suuri osa markkinoista myydään kerralla
        # Esim: jos on 1000 osaketta ja myyt 100, niin market_impact = 0.1 (10%)
        market_impact = shares_to_sell / (self.available_shares + shares_to_sell)
        logger.info(
            f"Market impact (sell): {market_impact:.3f} ({market_impact * 100:.1f}% of market)"
        )

        # 2. TARJONTA-KYSYNTÄ TEKIJÄ (käänteinen)
        # Mitä enemmän osakkeita on tarjolla, sitä halvempi hinta
        # Esim: jos on 150 osaketta (normaali=100), scarcity_factor = 0.67
        new_available_shares = self.available_shares + shares_to_sell
        scarcity_factor = normal_supply / new_available_shares
        logger.info(
            f"Scarcity factor (sell): {scarcity_factor:.3f} (normal supply: {normal_supply})"
        )

        # 3. LOGARITMINEN KASVU (käänteinen)
        # Estää liian jyrkät hinnanalennukset suurilla myynneillä
        log_factor = math.log(1 + shares_to_sell * market_sensitivity)
        logger.info(
            f"Log factor (sell): {log_factor:.3f} (shares: {shares_to_sell}, sensitivity: {market_sensitivity})"
        )

        # 4. SATUNNAINEN VOLATILITEETTI (sama kuin ostossa)
        volatility = random.uniform(-volatility_range, volatility_range)
        logger.info(f"Volatility (sell): {volatility:.3f} ({volatility * 100:.1f}%)")

        # YHDISTÄ KAIKKI TEKIJÄT (käänteinen vaikutus)
        # Myynti laskee hintaa, joten käytetään negatiivista muutosta
        total_change = -(
            market_impact * weights["market_impact"]
            + scarcity_factor * weights["scarcity_factor"]
            + log_factor * weights["log_factor"]
            + volatility * weights["volatility"]
        )

        # RAJOITA MUUTOS JÄRKEVÄÄN RAJAAN
        # Estää liian jyrkät hinnanalennukset (esim. max -20%)
        total_change = max(total_change, -max_price_change)
        logger.info(
            f"Total price change (sell): {total_change:.3f} ({total_change * 100:.1f}%)"
        )

        # PÄIVITÄ HINTA
        old_price = self.current_price
        self.current_price *= 1 + total_change
        self.available_shares += shares_to_sell  # Tarjonta kasvaa

        logger.info(f"Price changed from {old_price:.2f} to {self.current_price:.2f}")
        logger.info(f"Available shares: {self.available_shares}")

        return self.current_price

    def get_price(self):
        return self.current_price

    def get_available_shares(self):
        return self.available_shares

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_id(self):
        return self.id

    # Magic methods
    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.current_price:.2f} - {self.available_shares} shares"

    def __repr__(self):
        return f"Stock(name='{self.name}', symbol='{self.symbol}', price={self.current_price:.2f}, shares={self.available_shares})"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __len__(self):
        return self.available_shares


if __name__ == "__main__":
    stock = Stock(
        name="Tesla Inc.", symbol="TSLA", current_price=100.0, available_shares=1000
    )
    print(f"Initial: {stock}")
    print(f"After buying 10 shares: {stock.buy(10):.2f}")
    print(f"After selling 5 shares: {stock.sell(5):.2f}")
    print(f"Final: {stock}")
