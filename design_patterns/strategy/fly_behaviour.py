from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class SlowFlyBehaviour(FlyBehaviour):
    def fly(self):
        print('Slow Flying')


class FastFlyBehaviour(FlyBehaviour):
    def fly(self):
        print('Fast Flying')
