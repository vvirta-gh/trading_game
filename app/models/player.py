from typing import List
from models.stock import Stock


class Player:
    def __init__(self, name: str = "Trader", balance: float = 1000):
        self.name = name
        self.balance = balance
        self.portfolio = []

    

if __name__ == "__main__":
    player = Player()
    print(player.name)
    print(player.balance)
    print(player.portfolio)