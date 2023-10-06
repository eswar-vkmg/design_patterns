from abc import ABC, abstractmethod
from food_item import FoodItem
from iterator import DinnerMenuIterator, BreakfastMenuIterator


class Menu(ABC):
    @abstractmethod
    def add_food_item(self, food_item: FoodItem):
        pass

    @abstractmethod
    def get_iterator(self):
        pass


class BreakfastMenu(Menu):
    def __init__(self):
        self.breakfast_menu = []

    def add_food_item(self, food_item: FoodItem):
        self.breakfast_menu.append(food_item)

    def get_iterator(self):
        return BreakfastMenuIterator(self.breakfast_menu)


class DinnerMenu(Menu):
    def __init__(self):
        self.dinner_menu = {}

    def add_food_item(self, food_item: FoodItem):
        self.dinner_menu[food_item.name] = food_item

    def get_iterator(self):
        return DinnerMenuIterator(self.dinner_menu)
