import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Создает чистый экземпляр BooksCollector для каждого теста."""
    return BooksCollector()


@pytest.fixture
def collector_with_books():
    """Создает коллектор с предзаполненными книгами."""
    collector = BooksCollector()
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
def collector_with_favorites():
    """Создает коллектор с книгами в избранном."""
    collector = BooksCollector()
    books = ["Книга 1", "Книга 2", "Книга 3"]
    for book in books:
        collector.add_new_book(book)
    collector.add_book_in_favorites("Книга 1")
    collector.add_book_in_favorites("Книга 2")
    return collector