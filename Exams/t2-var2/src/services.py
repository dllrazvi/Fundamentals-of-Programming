import random

from src.repository import PlayerRepo

class Services:
    def __init__(self,repo):
        self._repo= repo

    def get_descending(self):
        sorted=self._repo.get
        sorted.sort(key= lambda x: x.strenght, reversed=True)
        return sorted
    def pair_players(self,list):
        pair=[]
        pair.append(random.choice(list))
        player=pair[0]
        ind=list.index(player)
        list.pop(ind)
        new_player = random.choice(list)
        pair.append(new_player)
        ind = list.index(new_player)
        list.pop(ind)
        return pair
    """
    This function firstly takes a random player, followed by removing it from the list containing  all the players by
      its index
    Then it takes another one and make the pair by doing SAME INSTRUCTIONS
    """
    def get(self):
        return self._repo.get()
repo=PlayerRepo(players.txt)
service=Player(repo)
Services.qualified()