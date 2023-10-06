from abc import ABC, abstractmethod


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass


class LowQuackBehavior(QuackBehaviour):
    def quack(self):
        print('Quacking in a low voice')


class HighQuackBehaviour(QuackBehaviour):
    def quack(self):
        print('Quacking in a high voice')
