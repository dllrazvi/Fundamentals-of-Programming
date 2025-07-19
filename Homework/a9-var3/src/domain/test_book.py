from .book import Book

class TestBook:
    def test_book(self):
        new_book = Book("1", "1984", "George Orwell")
        assert new_book.book_id == "1"
        assert new_book.title == "1984"
        assert new_book.author == "George Orwell"
        assert str(new_book) == "1. 1984 by George Orwell"

        new_book.title = "Animal Farm"
        assert new_book.title == "Animal Farm"
        assert str(new_book) == "1. Animal Farm by George Orwell"


if __name__ == "__main__":
    tests = TestBook()
    tests.test_book()