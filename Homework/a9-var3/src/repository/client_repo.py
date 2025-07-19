from src.domain.client import Client
from src.repository.repo_exception import RepoException

class ClientRepo:
    def __init__(self):
        self.__data = {}
    
    def add(self, new_client: Client):
        if new_client.client_id in self.__data:
            raise RepoException("Client already existing in repository")
        self.__data[new_client.client_id] = new_client
    
    def get_by_id(self, client_id) -> Client:
        try:
            return self.__data[client_id]
        except KeyError:
            raise RepoException(f"Client with id {client_id} not found.")
    
    def get_all(self) -> list[Client]:
        return list(self.__data.values())
    
    def __len__(self):
        return len(self.__data)
    
    def remove_by_id(self, client_id):
        if client_id in self.__data:
            del self.__data[client_id]
        else:
            raise RepoException(f"Client with id {client_id} not found.")
    
    def update(self, client: Client, client_id):
        if client_id in self.__data:
            self.__data[client_id] = client
        else:
            raise RepoException(f"Client with id {client_id} not found.")
    
    def clear(self):
        self.__data.clear()
    
    def add_sample_data(self):
        client1 = Client("1", "Client1")
        self.add(client1)
        client2 = Client("2", "Client2")
        self.add(client2)
        client3 = Client("3", "Client3")
        self.add(client3)
        client4 = Client("4", "Client4")
        self.add(client4)
        client5 = Client("5", "Client5")
        self.add(client5)
        client6 = Client("6", "Client6")
        self.add(client6)