from abc import abstractmethod, ABC


class Receiver(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class PhilipsLight(Receiver):
    def turn_on(self):
        print('Turning on philips light')

    def turn_off(self):
        print('Turning off philips light')


class IkeaLight(Receiver):
    def turn_on(self):
        print('Turning on Ikea Light')

    def turn_off(self):
        print('Turning off Ikea light')
