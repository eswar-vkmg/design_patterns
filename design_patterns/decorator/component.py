from abc import abstractmethod


class Beverage:
    def __init__(self):
        self.name = 'Beverage'

    def describe(self):
        return self.name

    @abstractmethod
    def cost(self):
        pass


class Coffee(Beverage):
    def __init__(self):
        super(Coffee, self).__init__()
        self.name = 'Coffee'

    def cost(self):
        return 7


class Tea(Beverage):
    def __init__(self):
        super(Tea, self).__init__()
        self.name = 'Tea'

    def cost(self):
        return 5
