from abc import ABC, abstractmethod
from food_item import FoodItem


class Menu(ABC):
    @abstractmethod
    def add_food_item(self, food_item: FoodItem):
        pass


class BreakfastMenu(Menu):
    def __init__(self):
        self.breakfast_menu = []

    def add_food_item(self, food_item: FoodItem):
        self.breakfast_menu.append(food_item)

    def __iter__(self):
        self.index = 0
        self.max_len = len(self.breakfast_menu)
        return self

    def __next__(self):
        if self.index >= self.max_len:
            raise StopIteration
        food_item = self.breakfast_menu[self.index]
        self.index += 1
        return food_item


class DinnerMenu(Menu):
    def __init__(self):
        self.dinner_menu = {}

    def add_food_item(self, food_item: FoodItem):
        self.dinner_menu[food_item.name] = food_item

    def __iter__(self):
        self.food_names = list(self.dinner_menu.keys())
        self.index = 0
        self.max_food_items = len(self.food_names)
        return self

    def __next__(self):
        if self.index >= self.max_food_items:
            raise StopIteration
        food_name = self.food_names[self.index]
        food_item = self.dinner_menu[food_name]
        self.index += 1
        return food_item
