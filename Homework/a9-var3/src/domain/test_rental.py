from .rental import Rental 
from .book import Book
from .client import Client
from datetime import date

class TestRental:
    def test_rental(self):
        book = Book("1", "1984", "George Orwell")
        client = Client("1", "Tom")

        rental = Rental("1", "1", "1", date(2022, 10, 15), date(2022, 10, 22), book, client)
        assert rental.book_id == "1"
        assert rental.client_id == "1"
        assert rental.rental_id == "1"
        assert len(rental) == 8

        rental = Rental(1, 1, 1, date.today(), None, book, client)
        assert len(rental) == 1
        
if __name__ == "__main__":
    tests = TestRental()
    tests.test_rental()