from .client import Client
import pytest

class TestClient():
    def test_client(self):
        new_client = Client("1", "Tom")
        assert new_client.client_id == "1"
        assert new_client.name == "Tom"
        assert str(new_client) == "1 -> Tom"

        new_client.name = "William"
        assert new_client.name == "William"
        assert str(new_client) == "1 -> William"
        
if __name__ == "__main__":
    tests = TestClient()
    tests.test_client()

    
