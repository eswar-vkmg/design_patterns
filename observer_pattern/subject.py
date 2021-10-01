class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def send_notification(self):
        for observer in self.observers:
            observer.update(self)


class CricketScore(Subject):
    def __init__(self):
        super(CricketScore, self).__init__()
        self.observers = []
        self.__runs = 0
        self.__wickets = 0

    @property
    def runs(self):
        return self.__runs

    @runs.setter
    def runs(self, value):
        self.__runs = value
        self.send_notification()

    @property
    def wickets(self):
        return self.__wickets

    @wickets.setter
    def wickets(self, value):
        self.__wickets = value
        self.send_notification()
