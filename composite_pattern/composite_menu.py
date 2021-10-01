from abc import ABC, abstractmethod


class CompositeMenu(ABC):
    @abstractmethod
    def add_menu_components(self, menu_component):
        pass

    @abstractmethod
    def remove_menu_component(self, menu_component):
        pass

    @abstractmethod
    def display(self):
        pass
