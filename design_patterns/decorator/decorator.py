# Decorator IS-A component
# Decorator HAS-A component

from abc import abstractmethod
from component import Beverage


class AddOn(Beverage):
    def __init__(self, beverage: Beverage):
        super(AddOn, self).__init__()
        self.beverage = beverage

    @abstractmethod
    def describe(self):
        return self.beverage.describe() + ": " + self.name

    @abstractmethod
    def cost(self):
        pass


class WhippedCream(AddOn):
    def __init__(self, beverage: Beverage):
        super(WhippedCream, self).__init__(beverage)
        self.name = 'Whipped Cream'
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 3


class Soy(AddOn):
    def __init__(self, beverage: Beverage):
        super(Soy, self).__init__(beverage)
        self.name = 'Soy'
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 2

