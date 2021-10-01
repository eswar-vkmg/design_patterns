import random


class WinnerLogic:
    def __init__(self):
        self.random_number = random.randint(0, 30)

    def is_a_winner(self):
        return self.random_number % 4 == 0
