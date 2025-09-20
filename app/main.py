from loguru import logger
from random import random
from app.ui.game_interface import GameInterface
from app.game import Game


def generate_random_number():
    return random()


def main():
    game = Game()
    game.run_game()

if __name__ == "__main__":
    main()
