from composite_menu import CompositeMenu


class Menu(CompositeMenu):
    def __init__(self, name):
        self.name = name
        self.menu_components = []

    def add_menu_components(self, menu_components):
        self.menu_components.extend(menu_components)

    def remove_menu_component(self, menu_component):
        self.menu_components.remove(menu_component)

    def display(self):
        print(f"--------- {self.name} ---------")
        for menu_component in self.menu_components:
            menu_component.display()
