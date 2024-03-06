from lib.book_store import *


def test_book_constructs():
    book = BookStore(1, "Test Book Title", "Test Author Name")
    book.id == 1
    book.title == "Test Book Title"
    book.author_name == "Test Author Name"

