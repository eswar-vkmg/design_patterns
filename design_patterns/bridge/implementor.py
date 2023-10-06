from abc import ABC, abstractmethod
from album import Album
from book import Book


class Resource(ABC):
    @abstractmethod
    def snippet(self):
        pass

    @abstractmethod
    def title(self):
        pass


class AlbumResource(Resource):
    def __init__(self, album_instance: Album):
        self.album_instance = album_instance

    def snippet(self):
        return self.album_instance.get_album_description()

    def title(self):
        return self.album_instance.get_album_name()


class BookResource(Resource):
    def __init__(self, book_instance: Book):
        self.book_instance = book_instance

    def snippet(self):
        return self.book_instance.get_book_overview()

    def title(self):
        return self.book_instance.get_book_name()
