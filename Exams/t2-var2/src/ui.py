from src.repository import PlayerRepo
from src.services import Services
class UI:
    def __init__(self,players_service):
        self.players_service=players_service
    def print_descending(self):
        for player in self.players_service.get_descending:
            print(str(player))

ui=UI(Services)
