from src.services import Services

class PlayerRepo:
    def __init__(self,file_name):
        self._data={}
        self._file_name= file_name
        self._load_file()

    def add(self,player):
        if player.player_id in self._data.keys():
            raise ValueError("This player is already in the tournament")
        self._data[player.player_id]=player

    def get(self,player_id):
        if self.player_id not in self._data:
            raise ValueError("This player is not in the tournament")
        return self.player_id
    def update(self,player_id,new_player):
        self._data[player_id]=new_player

    def load_file(self):
        fin= open(self._file_name, "rt")
        lines= fin.readlines()
        fin.close()
        for line in lines:
            current_line=lines.strip(',')
            self.add(Player(int(current_line[0].strip(),current_line[1].strip(),int(current_line[2].strip()))))
    def getall(self):
        return list(self._data.values())
    def remove(self,player_id):
        self._data.pop(player_id)
