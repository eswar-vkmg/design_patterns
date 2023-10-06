from abc import ABC, abstractmethod
from typing import Type
from implementor import Resource


class View(ABC):
    def __init__(self, resource: Resource):
        self.resource = resource

    @abstractmethod
    def show(self):
        pass


class ShortView(View):
    def __init__(self, resource: Resource):
        super().__init__(resource)

    def show(self):
        short_view = self.resource.title()
        print(f'Short View : {short_view}')


class LongView(View):
    def __init__(self, resource: Resource):
        super().__init__(resource)

    def show(self):
        long_view = self.resource.title() + " - " + self.resource.snippet()
        print(f'Long View : {long_view}')
