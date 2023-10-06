from menu import BreakfastMenu, DinnerMenu
from food_item import FoodItem

if __name__ == '__main__':
    # Breakfast Menu

    bf_menu = BreakfastMenu()
    bf_menu.add_food_item(FoodItem('Egg', 'omelette', 10))
    bf_menu.add_food_item(FoodItem('Dosa', 'Freshly made', 20))

    for food_item in iter(bf_menu):
        print(food_item.name)

    # Dinner Menu

    dinner_menu = DinnerMenu()
    dinner_menu.add_food_item(FoodItem('Chicken', 'Fried chicken', 30))
    dinner_menu.add_food_item(FoodItem('Parotta', 'Bun parotta', 40))

    for food_item in iter(dinner_menu):
        print(food_item.name)
