import sys
sys.path.append(".")
from src.domain.book import Book
from src.repository.book_repo import BookRepo

class TestBookRepo:
    def test_add(self):     
        repo = BookRepo()

        book = Book("1", "BookTitle", "BookAuthor")

        repo.add(book)

        books = repo.get_all()

        assert books[0].book_id == "1"
        assert books[0].title == "BookTitle"
        assert books[0].author == "BookAuthor"

    def test_get_by_id(self):
        repo = BookRepo()
        book_to_add = Book("1", "BookTitle", "BookAuthor")
        repo.add(book_to_add)

        book = repo.get_by_id("1")

        assert book is book_to_add
        
    def test_get_all(self):
        repo = BookRepo()
        book1 = Book("1", "BookTitle", "BookAuthor")
        book2 = Book("2", "The Castle", "BookAuthor")
        repo.add(book1)
        repo.add(book2)

        books = repo.get_all()
        assert books[0] == book1
        assert books[1] == book2
        assert len(books) == 2

    def test_remove_by_id(self):
        repo = BookRepo()
        book_to_add = Book("1", "BookTitle", "BookAuthor")
        repo.add(book_to_add)        

        assert len(repo) == 1

        repo.remove_by_id("1")

        assert len(repo) == 0
    
    def test_update(self):
        repo = BookRepo()
        book = Book("1", "BookTitle", "BookAuthor")
        repo.add(book)    
        book.author = "BookAuthor 2"

        repo.update(book, book.book_id)
        assert repo.get_by_id("1").author == "BookAuthor 2"

if __name__ == "__main__":
    tests = TestBookRepo()
    tests.test_add()
    tests.test_get_by_id()
    tests.test_get_all()
    tests.test_remove_by_id()
    tests.test_update()