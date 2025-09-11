from loguru import logger
from random import random


def generate_random_number():
    return random()

def main():
    logger.info(f"Random number: {generate_random_number()}")

if __name__ == "__main__":
    main()    