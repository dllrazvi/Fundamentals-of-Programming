from src.services.clients_service import ClientsService
from src.repository.client_repo import ClientRepo
class TestClientsService:
    def __init__(self):
        repo = ClientRepo()
        self._service = ClientsService(repo)

    def test_add(self):
        self._service.add("ClientTest")
        assert len(self._service.list()) == 1
    
    def test_remove(self):
        self._service.clear()
        self._service.add("ClientTest")
        assert len(self._service.list()) == 1
        self._service.remove("1")
        assert len(self._service.list()) == 0
    
    def test_update(self):
        self._service.clear()
        self._service.add("ClientTest")
        assert self._service.find_by_id("1").name == "ClientTest"
        self._service.update("1", "Client Test")
        assert self._service.find_by_id("1").name == "Client Test"

    

