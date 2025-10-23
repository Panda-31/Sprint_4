from main import BooksCollector
import pytest


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # ИСПРАВЛЕНИЕ: используем get_books_genre() вместо get_books_rating()
        assert len(collector.get_books_genre()) == 2        
    @pytest.mark.parametrize('book_name', [
        'Книга',
        'Очень интересная книга',
        'A' * 40,
        '   '
    ])
    def test_add_new_book_valid_names_book_added_with_empty_genre(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('invalid_name', [
        '',
        'A' * 41,

    ])
    def test_add_new_book_invalid_names_book_not_added(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    def test_add_new_book_duplicate_book_not_added(self):
        collector = BooksCollector()
        book_name = "1984"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_book_and_genre_genre_set(self):
        collector = BooksCollector()
        book_name = "Преступление и наказание"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre_genre_not_set(self):
        collector = BooksCollector()
        book_name = "Мастер и Маргарита"
        invalid_genre = "Роман"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Фантастика 1")
        collector.add_new_book("Фантастика 2")
        collector.set_book_genre("Фантастика 1", "Фантастика")
        collector.set_book_genre("Фантастика 2", "Фантастика")
        
        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert "Фантастика 1" in fantasy_books
        assert "Фантастика 2" in fantasy_books
        assert len(fantasy_books) == 2

    def test_get_books_for_children_excludes_age_restricted_books(self):
        collector = BooksCollector()
        collector.add_new_book("Мультик")
        collector.add_new_book("Страшилка")
        collector.set_book_genre("Мультик", "Мультфильмы")
        collector.set_book_genre("Страшилка", "Ужасы")
        
        children_books = collector.get_books_for_children()
        assert "Мультик" in children_books
        assert "Страшилка" not in children_books

    def test_add_and_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
        
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()