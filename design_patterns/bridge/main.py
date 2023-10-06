from abstraction import ShortView, LongView
from implementor import AlbumResource, BookResource
from album import Album
from book import Book


if __name__ == "__main__":

    # -- For 1 type of resource

    album = Album(name='After Hours', desc='Mind blowing psychedelic chapter')
    album_resource = AlbumResource(album)

    short_view = ShortView(album_resource)
    short_view.show()

    long_view = LongView(album_resource)
    long_view.show()

    # -- For another type of resource

    book = Book(name='Harry Potter', desc='Wizarding World Wonder')
    book_resource = BookResource(book)

    short_view = ShortView(book_resource)
    short_view.show()

    long_view = LongView(book_resource)
    long_view.show()
