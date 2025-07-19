from src.domain.book import Book
from src.repository.repo_exception import RepoException

class BookRepo:
    def __init__(self):
        self.__data = {}
    
    def add(self, new_book: Book):
        if new_book.book_id in self.__data:
            raise RepoException("Book already existing in repository")
        self.__data[new_book.book_id] = new_book
    
    def get_by_id(self, book_id) -> Book:
        try:
            return self.__data[book_id]
        except KeyError:
            raise RepoException(f"Book with id {book_id} not found.")
        
    def get_all(self) -> list[Book]:
        return list(self.__data.values())
    
    def __len__(self):
        return len(self.__data)
    
    def remove_by_id(self, book_id):
        if book_id in self.__data:
            del self.__data[book_id]
        else:
            raise RepoException(f"Book with id {book_id} not found.")
    
    def update(self, book: Book, book_id):
        if book_id in self.__data:
            self.__data[book_id] = book
        else:
            raise RepoException(f"Book with id {book_id} not found.")
    
    def clear(self):
        self.__data.clear()

    def add_sample_data(self):
        book1 = Book("1", "Book1", "Author1")
        book2 = Book("2", "Book2", "Author1")
        book3 = Book("3", "Book3", "Author2")
        book4 = Book("4", "Book4", "Author3")
        book5 = Book("5", "Book5", "Author3")
        book6 = Book("6", "Book6", "Author3")
        book7 = Book("7", "Book7", "Author3")

        self.add(book1)
        self.add(book2)
        self.add(book3)
        self.add(book4)
        self.add(book5)
        self.add(book6)
        self.add(book7)