from abc import ABC, abstractmethod
from receiver import Receiver


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_on()


class TurnOffCommand(Command):
    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_off()
