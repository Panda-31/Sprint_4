from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', [
        'Книга',
        'Очень интересная книга',
        'A' * 40,
        '   '
    ])
    def test_add_new_book_valid_names_book_added_with_empty_genre(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('invalid_name', [
        '',
        'A' * 41,
    ])
    def test_add_new_book_invalid_names_book_not_added(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    def test_add_new_book_duplicate_book_not_added(self, collector):
        book_name = "1984"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_book_and_genre_genre_set(self, collector):
        book_name = "Преступление и наказание"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre_genre_not_set(self, collector):
        book_name = "Мастер и Маргарита"
        invalid_genre = "Роман"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre_returns_correct_books(self, collector_with_books):
        fantasy_books = collector_with_books.get_books_with_specific_genre("Фантастика")
        assert "Война и мир" in fantasy_books
        assert len(fantasy_books) == 1

    def test_get_books_for_children_excludes_age_restricted_books(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert "Том и Джерри" in children_books
        assert "Оно" not in children_books
        assert "Шерлок Холмс" not in children_books

    def test_add_book_in_favorites_valid_book_added(self, collector):
        book_name = "Гарри Поттер"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book_not_added(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_existing_book_removed(self, collector_with_book_in_favorites):
        collector, book_name = collector_with_book_in_favorites
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book_no_error(self, collector):
        collector.delete_book_from_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()