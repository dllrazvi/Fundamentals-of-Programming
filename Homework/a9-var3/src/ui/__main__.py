import sys
sys.path.append(".")
from src.repository.book_repo import *
from src.repository.client_repo import *
from src.repository.rental_repo import *
from src.services.books_service import *
from src.services.clients_service import *
from src.services.rentals_service import *
from src.ui.ui import Ui
import random
from datetime import date, timedelta
from src.services import rentals_service
class Program:
    def __init__(self):
        self.books_service = BooksService(BookRepo())
        self.clients_service = ClientsService(ClientRepo())
        self.rentals_service = RentalService(RentalRepo(), self.books_service, self.clients_service)
    def main(self):
        client_repo = ClientRepo()
        client_repo.add_sample_data()
        client_service = ClientsService(client_repo)

        book_repo = BookRepo()
        book_repo.add_sample_data()
        book_service = BooksService(book_repo)

        rental_repo = RentalRepo()
        rental_service = RentalService(rental_repo, book_service, client_service)
        ui = Ui(self.books_service, self.clients_service, self.rentals_service)
        ui.run()
if __name__ == "__main__":
    p = Program()
    p.main()
