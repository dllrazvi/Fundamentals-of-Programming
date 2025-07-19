from src.domain.rental import Rental
from src.repository.repo_exception import RepoException
from datetime import date

class RentalRepo:
    def __init__(self):
        self.__data = {}
    
    def add(self, new_rental: Rental):
        if new_rental.rental_id in self.__data:
            raise RepoException("Rental already existing in repository.")
        self.__data[new_rental.rental_id] = new_rental
    
    def get_by_id(self, rental_id):
        try:
            return self.__data[rental_id]
        except KeyError:
            raise RepoException(f"Rental with {rental_id} not found.")
    
    def get_all(self) -> list[Rental]:
        return list(self.__data.values())
    
    def __len__(self):
        return len(self.__data)

    def remove_by_id(self, rental_id):
        if rental_id in self.__data:
            del self.__data[rental_id]
        else:
            raise RepoException(f"Rental with {rental_id} not found.")

    def update(self, rental: Rental, rental_id):
        if rental_id in self.__data:
            self.__data[rental_id] = rental
        else:
            raise RepoException(f"Rental with id {rental_id} not found.")

