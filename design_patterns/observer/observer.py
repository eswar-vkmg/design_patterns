from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self):
        pass


class Observer:
    def __init__(self):
        self.name = None

    @abstractmethod
    def update_temperature(self, subject_obj):
        pass


class SamsungDisplay(Display, Observer):
    def __init__(self):
        super(SamsungDisplay, self).__init__()
        self.name = 'Samsung-Display'
        self.temperature = 0

    def update_temperature(self, weather_station_obj):
        self.temperature = weather_station_obj.temperature
        self.display()

    def display(self):
        print(f'Temperature in {self.name} has been updated to {self.temperature}')


class LGDisplay(Display, Observer):
    def __init__(self):
        super(LGDisplay, self).__init__()
        self.name = 'LG-Display'
        self.temperature = 0

    def update_temperature(self, weather_station_obj):
        self.temperature = weather_station_obj.temperature
        self.display()

    def display(self):
        print(f'Temperature from {self.name} has been updated to {self.temperature}')
