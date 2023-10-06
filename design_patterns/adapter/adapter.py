from adaptee import Adaptee
from typing import Type


class AddNumbers:
    def __init__(self, vals, target: Type[Adaptee]):
        self.vals = vals
        self.target = target

    def add_nums(self):
        a = self.vals[0]
        b = self.vals[1]
        return self.target.add_numbers(a, b)
