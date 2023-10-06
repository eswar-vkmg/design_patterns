import math
from abc import ABC, abstractmethod


class Adaptee(ABC):
    @staticmethod
    @abstractmethod
    def add_numbers(a, b):
        pass


class AddNumbersV2(Adaptee):
    @staticmethod
    def add_numbers(a, b):
        return a + b


class AddNumbersV3(Adaptee):
    @staticmethod
    def add_numbers(a, b):
        return math.floor(a) + math.floor(b)
