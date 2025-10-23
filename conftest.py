import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    books = [
        ("Война и мир", "Фантастика"),
        ("Оно", "Ужасы"),
        ("Том и Джерри", "Мультфильмы"),
        ("Шерлок Холмс", "Детективы")
    ]
    for book_name, genre in books:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector


@pytest.fixture
def collector_with_favorites(collector):
    books = ["Книга 1", "Книга 2", "Книга 3"]
    for book in books:
        collector.add_new_book(book)
    collector.add_book_in_favorites("Книга 1")
    collector.add_book_in_favorites("Книга 2")
    return collector


@pytest.fixture
def collector_with_book_in_favorites(collector):
    book_name = "Тестовая книга"
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    return collector, book_name