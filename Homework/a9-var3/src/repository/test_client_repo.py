import sys
sys.path.append(".")
from src.domain.client import Client
from src.repository.client_repo import ClientRepo

class TestClientRepo:
    def test_add(self):
        repo = ClientRepo()
        assert len(repo) == 0
        client = Client("5", "Test")
        repo.add(client)

        assert len(repo) == 1
    

    def test_get_by_id(self):
        repo = ClientRepo()
        client_to_add = Client("5", "Test")
        repo.add(client_to_add)

        client = repo.get_by_id("5")
        assert client.client_id == "5"
        assert client.name == "Test"
    
    def test_remove_by_id(self):
        repo = ClientRepo()
        client_to_add = Client("5", "Test")
        repo.add(client_to_add)

        assert len(repo) == 1

        repo.remove_by_id("5")

        assert len(repo) == 0
    
    def test_update(self):
        repo = ClientRepo()
        client = Client("5", "Test")
        repo.add(client)

        client.name = "Test2"

        repo.update(client, client.client_id)

        assert repo.get_by_id("5").name == "Test2"



if __name__ == "__main__":
    tests = TestClientRepo()
    tests.test_add()
    tests.test_get_by_id()