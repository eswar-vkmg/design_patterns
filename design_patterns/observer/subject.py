from observer import Observer


class Subject:
    def __init__(self):
        self.observers = []

    def add(self, observer: Observer):
        print(f"Adding {observer.name} to the list")
        self.observers.append(observer)

    def remove(self, observer: Observer):
        print(f"Removing {observer.name} to the list")
        self.observers.remove(observer)

    def notify(self, child_obj):
        for observer in self.observers:
            print(f"Sending update to {observer.name}")
            observer.update_temperature(child_obj)


class WeatherStation(Subject):
    def __init__(self):
        super(WeatherStation, self).__init__()
        self.__temperature = 0

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        print(f'Setting weather station temp to {value}')
        self.__temperature = value
        self.notify(self)
