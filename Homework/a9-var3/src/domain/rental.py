from .book import Book
from .client import Client
from datetime import date

class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date, book: Book, client: Client):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date
        self.__book = book
        self.__client = client
    
    @property
    def rental_id(self):
        return self.__rental_id
    
    @property
    def book_id(self):
        return self.__book_id
    
    @book_id.setter
    def book_id(self, new_value):
        self.__book_id = new_value
    
    @property
    def client_id(self):
        return self.__client_id
    
    @client_id.setter
    def client_id(self, new_value):
        self.__client_id = new_value

    @property
    def rented_date(self):
        return self.__rented_date
    
    @rented_date.setter
    def rented_date(self, new_value):
        self.__rented_date = new_value
    
    @property
    def returned_date(self):
        return self.__returned_date()
    
    @returned_date.setter
    def returned_date(self, new_value):
        self.__returned_date = new_value

    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, new_value):
        self.__book = new_value
    
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, new_value):
        self.__client = new_value
    
    def __str__(self):
        return "Rental: " + str(self.rental_id) + "\nBook: " + str(self.book) + "\nClient: " + str(
            self.client) + "\nPeriod: " + self.__rented_date.strftime("%Y-%m-%d") + " to " + self.__returned_date.strftime("%Y-%m-%d")

    def __len__(self):
        if self.__returned_date is not None:
            return (self.__returned_date - self.__rented_date).days + 1
        today = date.today()
        return (today - self.__rented_date).days + 1

    def __repr__(self):
        return str(self)