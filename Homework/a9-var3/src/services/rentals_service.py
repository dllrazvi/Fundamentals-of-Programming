from src.repository.rental_repo import RentalRepo
from src.domain.rental import Rental
from src.domain.book import Book
from src.domain.client import Client
from src.services.books_service import BooksService
from src.services.clients_service import ClientsService
from src.services.service_exception import ServiceException

class RentalService:
    def __init__(self, repo: RentalRepo, books_service: BooksService, clients_service: ClientsService):
        self.__repo = repo
        self.__books_service = books_service
        self.__clients_service = clients_service
    
    def add(self, rented_date, returned_date, book: Book, client: Client):
        new_rental = Rental(str(len(self.__repo) + 1), book.book_id, client.client_id, rented_date, returned_date, book, client)

        self.__repo.add(new_rental)

    def remove(self, rental_id):
        self.__repo.remove_by_id(rental_id)
    
    def update(self, rental: Rental):
        self.__repo.update(rental, rental.rental_id)
    
    def list(self) -> list[Rental]:
        return self.__repo.get_all()

    def rent_book(self, rented_date, book_id, client_id):
        self.__books_service.find_by_id(book_id)
        self.__clients_service.find_by_id(client_id)

        available = self.is_available_for_rental(book_id)
        if not available:
            raise ServiceException(f"Book with id {book_id} is not available to rent.")

        # Find book
        book = self.__books_service.find_by_id(book_id)

        # Find client
        client = self.__clients_service.find_by_id(client_id)

        # Create rental
        self.add(rented_date, None, book, client)

    def return_book(self, book_id, returned_date):
        self.__books_service.find_by_id(book_id)
        rentals = self.list()
        for rental in rentals:
            if rental.book_id == book_id:
                rental.returned_date = returned_date
                self.update(rental)
                break
        
    def is_available_for_rental(self, book_id):
        rentals = self.list()
        for rental in rentals:
            if rental.book_id == book_id:
                if rental.returned_date is None:
                    return False
                break
        return True

    def most_rented_books(self):
        rented_books = []
        rentals = self.list()
        rent_count = {}
        for rental in rentals:
            if rental.book_id not in rent_count:
                rent_count[rental.book_id] = 1
            else:
                rent_count[rental.book_id] += 1
        sorted_rent_count = dict(sorted(rent_count.items(), key=lambda x:x[1], reverse=True))
        for r in sorted_rent_count:
            book = self.__books_service.find_by_id(r)
            rented_books.append(BooksRentalDto(book, sorted_rent_count[r]))
        
        return rented_books

    def most_active_clients(self):
        clients = []
        rentals = self.list()
        clients_rentals = {}
        for rental in rentals:
            if rental.client_id not in clients_rentals:
                clients_rentals[rental.client_id] = 1
            else:
                clients_rentals[rental.client_id] += 1
        sorted_clients_rentals = dict(sorted(clients_rentals.items(), key=lambda x:x[1], reverse=True))
        for r in sorted_clients_rentals:
            client = self.__clients_service.find_by_id(r)
            clients.append(ClientRentalsDto(client, sorted_clients_rentals[r]))

        return clients

    def most_rented_author(self):
        rentals = self.list()
        author_rentals = {}
        for rental in rentals:
            if rental.book.author not in author_rentals:
                author_rentals[rental.book.author] = 1
            else:
                author_rentals[rental.book.author] += 1
        sorted_author_rentals = dict(sorted(author_rentals.items(), key=lambda x:x[1], reverse=True))
        
        return next(iter(sorted_author_rentals))


class BooksRentalDto:
    def __init__(self, book: Book, count):
        self._book = book
        self._count = count
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, new_value):
        self._count = new_value
    
    def __repr__(self):
        return str(self._book) + " was rented " + str(self._count) + " times."

class ClientRentalsDto:
    def __init__(self, client: Client, count):
        self._client = client
        self._count = count
     
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, new_value):
        self._count = new_value

    def __repr__(self):
        return str(self._client) + " rented " + str(self._count) + " times."

