from composite_menu import CompositeMenu


class MenuItem(CompositeMenu):
    def __init__(self, name, is_veg, price):
        self.name = name
        self.is_veg = is_veg
        self.price = price

    def add_menu_components(self, menu_components):
        print('Unsupported operation')

    def remove_menu_component(self, menu_component):
        print('Unsupported operation')

    def display(self):
        classification = 'Veg' if self.is_veg else 'NonVeg'
        print(' - '.join([self.name, classification, str(self.price)]))
