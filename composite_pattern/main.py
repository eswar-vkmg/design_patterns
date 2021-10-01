from menuItems import MenuItem
from menu import Menu
from waitress import Waitress

if __name__ == '__main__':
    pancake = MenuItem(name='Pancake', is_veg=True, price=1)
    toast = MenuItem(name='Toast', is_veg=True, price=2)
    breakfast_menu = Menu(name='Breakfast Menu')
    breakfast_menu.add_menu_components([pancake, toast])

    steak = MenuItem(name='Steak', is_veg=False, price=3)
    roti = MenuItem(name='Roti', is_veg=False, price=4)
    dinner_menu = Menu(name='Dinner Menu')
    dinner_menu.add_menu_components([steak, roti])

    pepsi = MenuItem(name='Pepsi', is_veg=True, price=5)
    coke = MenuItem(name='Coke', is_veg=True, price=6)
    beverages_menu = Menu(name='Beverages sub-menu')
    beverages_menu.add_menu_components([pepsi, roti])

    dinner_menu.add_menu_components([beverages_menu, ])

    main_menu = Menu(name='Main Menu')
    main_menu.add_menu_components([breakfast_menu, dinner_menu])

    waitress = Waitress(main_menu)
    waitress.display_order()
