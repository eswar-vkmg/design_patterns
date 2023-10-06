class Book:
    def __init__(self, name, desc):
        self.book_name = name
        self.overview = desc

    def get_book_name(self):
        return self.book_name

    def get_book_overview(self):
        return self.overview
