from abc import abstractmethod
from typing import final


class Beverage:
    @final
    def prepare_beverage(self):
        """ Not supposed to be over-ridden by child classes """
        self.boil_water()
        self.pour_in_cup()
        self.brew()
        self.add_condiments()

    @abstractmethod
    def boil_water(self):
        print('Boil water for 10 mins')

    @abstractmethod
    def pour_in_cup(self):
        print('Pour into 200ml cup')

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Tea(Beverage):
    def brew(self):
        print('Brew until thickens')

    def add_condiments(self):
        print('Adding cardamom and ginger')


class Milk(Beverage):
    def brew(self):
        print('Brew until thins')

    def add_condiments(self):
        print('Add sugar and boost')
