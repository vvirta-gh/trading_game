import uuid

class Stock:
    def __init__(self, name: str, symbol: str, current_price: float, count: int):
        self.id = uuid.uuid4()
        self.name = name
        self.symbol = symbol
        self.current_price = current_price
        self.count = count

    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.current_price} - {self.count}"