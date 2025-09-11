from random import random
from random import gauss
from rich import print

def generate_random_number() -> float:
    return  random() # float between 0 and 1


def generate_random_number_between_min_and_max(min: float, max: float) -> float:
    return random() * (max - min) + min


def generate_random_number_with_mean_and_std(mean: float, std: float) -> float:
    return gauss(mean, std)



if __name__ == "__main__":
    print("Random number between 0 and 1:", generate_random_number())
    print("Random number between min=0 and max=1:", generate_random_number_between_min_and_max(0, 1))
    print("Random number with mean=0 and std=1:", generate_random_number_with_mean_and_std(0, 1))