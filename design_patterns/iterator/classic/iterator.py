from abc import ABC, abstractmethod
from food_item import FoodItem


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def get_next(self) -> FoodItem:
        pass


class BreakfastMenuIterator(Iterator):
    def __init__(self, menu: list):
        self.menu = menu
        self.index = 0
        self.max_length = len(self.menu)

    def has_next(self) -> bool:
        return self.index < self.max_length

    def get_next(self) -> FoodItem:
        menu_item = self.menu[self.index]
        self.index += 1
        return menu_item


class DinnerMenuIterator(Iterator):
    def __init__(self, menu: dict):
        self.menu = menu
        self.food_names = list(menu.keys())
        self.all_food_length = len(self.food_names)
        self.index = 0

    def has_next(self) -> bool:
        return self.index < self.all_food_length

    def get_next(self) -> FoodItem:
        food_name = self.food_names[self.index]
        food_item = self.menu[food_name]
        self.index += 1
        return food_item
