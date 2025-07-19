from src.repository.client_repo import ClientRepo
from src.domain.client import Client

class ClientsService:
    def __init__(self, repo: ClientRepo):
        self.__repo = repo

    def add(self, name):
        new_client = Client(str(len(self.__repo) + 1), name)
        self.__repo.add(new_client)

    def remove(self, client_id):
        self.__repo.remove_by_id(client_id)

    def update(self, client_id, new_name):
        client = Client(client_id, new_name)
        self.__repo.update(client, client_id)
    
    def list(self):
        return self.__repo.get_all()
    
    def find_by_id(self, client_id):
        return self.__repo.get_by_id(client_id)
    
    def find_by_name(self, name):
        output = []
        clients = self.__repo.get_all()
        for client in clients:
            if name.lower() in client.name.lower():
                output.append(client)
        return output
    
    def clear(self):
        self.__repo.clear()

    