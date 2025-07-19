import random

from repo import Repository
from Domain import Domain
from serv import Service
class UI:
    def __init__(self, repo,serv):
        self.repo = Repository()
        self.serv = Service()
    def print_matrix(self):
        a=self.serv.print_table()

        for i in range (1,7):

           print('+---+---+---+---+---+---+')
           for j in range (1,7):
               if a[i][j]==0:
                   print ('|   ',end="")
               else:
                   print ('| '+str(a[i][j])+ ' ',end="")
           print('|')
        print('+---+---+---+---+---+---+')

    def start_game(self):
        while True:
            print("Current Matrix: ")
            self.print_matrix() #printing the matrix everytime a move is done and first
            possible_moves = self.repo.validity()
            print("Possible moves: ", possible_moves)
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            assert [x,y] in self.serv.validity(), "Wrong coordonated"
            v='X'
            self.serv.move(x,y,v) #putting the symbol in repo and implicit in matrix
            if self.serv.verify_win(x,y)==1: #verifing if there xists a win
                print("Order wins. Game finised")
            if self.serv.validity()== []: #checking if the board is full or not
                print("Board is full, chaos wins")
                return
            x,y= random.choice(self.serv.validity())

            self.serv.move(x,y,'O')

if __name__ == '__main__':
    repository = Repository()
    services = Service()
    ui = UI(repository, services)
    ui.start_game()