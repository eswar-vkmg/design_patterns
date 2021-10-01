from abc import ABC, abstractmethod


class RequestFormationStrategy(ABC):
    @abstractmethod
    def prepare_request_object(self):
        pass


class ExcelFormationStrategy(RequestFormationStrategy):
    def prepare_request_object(self):
        print('Preparing excel file')
