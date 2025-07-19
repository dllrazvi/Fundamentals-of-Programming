from src.services.books_service import BooksService
from src.repository.book_repo import BookRepo

class TestBooksService:
    def __init__(self):
        repo = BookRepo()
        self._service = BooksService(repo)

    def test_add(self):
        self._service.add("BookTest")
        assert len(self._service.list()) == 1
    
    def test_remove(self):
        self._service.clear()
        self._service.add("BookTest")
        assert len(self._service.list()) == 1
        self._service.remove("1")
        assert len(self._service.list()) == 0
    
    def test_update(self):
        self._service.clear()
        self._service.add("BookTest")
        assert self._service.find_by_id("1").name == "BookTest"
        self._service.update("1", "Book Test")
        assert self._service.find_by_id("1").name == "Book Test"

if __name__ == "__main__":
    tests = TestBooksService()
    tests.test_add()
    tests.test_remove()
    tests.test_update()