from abc import abstractmethod
from fly_behaviour import FlyBehaviour
from quack_behaviour import QuackBehaviour


class Duck:
    def __init__(self, quack_instance: QuackBehaviour, fly_instance: FlyBehaviour):
        self.quack_instance = quack_instance
        self.fly_instance = fly_instance

    @abstractmethod
    def perform_fly(self):
        pass

    @abstractmethod
    def perform_quack(self):
        pass


class ADuck(Duck):
    def perform_fly(self):
        print('ADuck flying')
        self.fly_instance.fly()

    def perform_quack(self):
        print('ADuck quacking')
        self.quack_instance.quack()


class BDuck(Duck):
    def perform_fly(self):
        print('BDuck flying')
        self.fly_instance.fly()

    def perform_quack(self):
        print('BDuck quacking')
        self.quack_instance.quack()


class CDuck(Duck):
    def perform_fly(self):
        print('CDuck flying')
        self.fly_instance.fly()

    def perform_quack(self):
        print('CDuck quacking')
        self.quack_instance.quack()
