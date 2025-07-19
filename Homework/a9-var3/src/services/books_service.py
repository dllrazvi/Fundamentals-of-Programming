from src.domain.book import Book
from src.repository.book_repo import BookRepo
from random import choice

class BooksService:
    def __init__(self, repo: BookRepo):
        self.__repo = repo
    
    def add(self, title, author):
        new_book = Book(str(len(self.__repo) + 1), title, author)
        
        self.__repo.add(new_book)
    
    def remove(self, book_id):
        self.__repo.remove_by_id(book_id)

    
    def update(self, id, title, author):
        book = Book(id, title, author)
        self.__repo.update(book, id)

    def list(self):
        return self.__repo.get_all()

    def find_by_id(self, book_id):
        return self.__repo.get_by_id(book_id)

        
    def find_by_title(self, title):
        output = []
        books = self.__repo.get_all()
        for book in books:
            if title.lower() in book.title.lower():
                output.append(book)
        return output

    def find_by_author(self, author):
        output = []
        books = self.__repo.get_all()
        for book in books:
            if author.lower() in book.author.lower():
                output.append(book)
        return output

    def clear(self):
        self.__repo.clear()

    def generate_books(self):
        authors = ["george","mihai","ion"]
        titles = ["Fairy Land","Nasul cat bucata de faianta","Mana care pute a bara de troleu"]

        result = []
        n=10
        while n < 20:
            author = choice(authors)
            title = choice(titles)

            result.append(Book(len(self.__repo) + 1, title, author))

            n -= 1
        
        return result