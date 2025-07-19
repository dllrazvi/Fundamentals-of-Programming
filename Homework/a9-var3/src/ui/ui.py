from src.services.books_service import *
from src.services.clients_service import *
from src.services.rentals_service import *
from datetime import date
class Ui:
    def __init__(self, books_service: BooksService, clients_service: ClientsService, rentals_service: RentalService):
        self.__books_service = books_service
        self.__clients_service = clients_service
        self.__rentals_service = rentals_service

        
    def print_main_menu(self):
        menu = """
        1. Manage clients
        2. Manage books
        3. Rent a book
        4. Return a book
        5. Search for a client by id
        6. Search for clients by name 
        7. Search for a book by id
        8. Search for a book by title
        9. Search for a book by author
        10. Most rented books
        11. Most active clients
        12. Most rented author
        """
        print(menu)

    def print_clients_menu(self):
        menu = """
        1. Add client
        2. Remove client
        3. Update client
        4. List clients
        """
        print(menu)
    
    def print_books_menu(self):
        menu = """
        1. Add book
        2. Remove book
        3. Update book
        4. List books
        """
        print(menu)
    
    def run(self):
        while True:
            self.print_main_menu()
            option = input()

            # Manage Clients
            if option == "1":
                self.print_clients_menu()
                opt = input()

                # Add
                if opt == "1":
                    name = input("Name: ")
                    try:
                        self.__clients_service.add(name)
                    except Exception as e:
                        print(e)

                # Remove
                elif opt == "2":
                    id = input("Id:")
                    try:
                        self.__clients_service.remove(id)
                    except Exception as e:
                        print(e)

                # Update
                elif opt == "3":
                    id = input("Client id:")
                    name = input("New name: ")
                    try:
                        self.__clients_service.update(id, name)
                    except Exception as e:
                        print(e)
                
                # List
                elif opt == "4":
                    clients = self.__clients_service.list()
                    for client in clients:
                        print(client)
            
            # Manage books
            elif option == "2":
                self.print_books_menu()
                opt = input()

                # Add
                if opt == "1":
                    title = input("Title: ")
                    author = input("Author: ")
                    try:
                        self.__books_service.add(title, author)
                    except Exception as e:
                        print(e)
                
                # Remove
                elif opt == "2":
                    id = input("Id: ")
                    try:
                        self.__books_service.remove(id)
                    except Exception as e:
                        print(e)
                
                # Update
                elif opt == "3":
                    id = input("Book id: ")
                    title = input("New title: ")
                    author = input("New author: ")
                    try:
                        self.__books_service.update(id, title, author)
                    except Exception as e:
                        print(e)
                
                # List
                elif opt == "4":
                    books = self.__books_service.list()
                    for book in books:
                        print(book)
            # Rent a book
            elif option == "3":
                book_id = input("Book Id: ")
                client_id = input("Client Id: ")
                try:
                    self.__rentals_service.rent_book(date.today(), book_id, client_id)
                except Exception as e:
                    print(e)
            
            # Return a book
            elif option == "4":
                book_id = input("Book Id: ")
                try:
                    self.__rentals_service.return_book(book_id, date.today())
                except Exception as e:
                    print(e)
            
            # Search client by id:
            elif option == "5":
                id = input("Client Id:")
                try:
                    client = self.__clients_service.find_by_id(id)
                except Exception as e:
                    print(e)
            
            # Search clients by name:
            elif option == "6":
                name = input("Name: ")
                clients = []
                try:
                    clients = self.__clients_service.find_by_name(name)
                except Exception as e:
                    print(e)
                for cl in clients:
                    print(cl)

            # Search book by id
            elif option == "7":
                id = input("Id: ")
                try:
                    book = self.__books_service.find_by_id(id)
                    print(book)
                except Exception as e:
                    print(e)
            
            # Search book by title
            elif option == "8":
                title = input("Title: ")
                try:
                    book = self.__books_service.find_by_title(title)
                    print(book)
                except Exception as e:
                    print(e)

            # Search by author
            elif option == "9":
                author = input("Author: ")
                try:
                    book = self.__books_service.find_by_author(author)
                    print(book)
                except Exception as e:
                    print(e)
            
            # Most rented books
            elif option == "10":
                books = []
                try:
                    books = self.__rentals_service.most_rented_books()
                except Exception as e:
                    print(e)
                for b in books:
                    print(b)
            
            # Most active clients
            elif option == "11":
                clients = []
                try:
                    clients = self.__rentals_service.most_active_clients()
                except Exception as e:
                    print(e)
                for c in clients:
                    print(c)
            
            # Most rented author
            elif option == "12":
                author = self.__rentals_service.most_rented_author()
                print(author)






