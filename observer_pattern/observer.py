from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject_obj):
        pass


class RunsDisplay(Display, Observer):
    def __init__(self, subject_obj):
        self.runs = 0
        subject_obj.add_observer(self)

    def update(self, cricket_score_obj):
        self.runs = cricket_score_obj.runs
        self.display()

    def display(self):
        print(f'{self.runs} runs are scored')


class WicketsDisplay(Display, Observer):
    def __init__(self, subject_obj):
        self.wickets = 0
        subject_obj.add_observer(self)

    def update(self, cricket_score_obj):
        self.wickets = cricket_score_obj.wickets
        self.display()

    def display(self):
        print(f'{self.wickets} wickets are taken')
