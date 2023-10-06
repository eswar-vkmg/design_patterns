from subject import BookParser, RealBookParser


class LazyBookParser(BookParser):
    def __init__(self):
        print('Lazy book parser init')
        self.real_book_parser = None

    def get_number_of_pages(self):
        if self.real_book_parser is None:
            self.real_book_parser = RealBookParser()  # Deferring the actual exp obj creation until method is called
        return self.real_book_parser.get_number_of_pages()
