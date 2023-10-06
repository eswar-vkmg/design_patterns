from abc import abstractmethod, ABC


class BookParser(ABC):
    @abstractmethod
    def get_number_of_pages(self):
        pass


class RealBookParser(BookParser):
    def __init__(self):
        print('Really expensive operation...')

    def get_number_of_pages(self):
        print('Cheap operation')
        return 'No of pages'
