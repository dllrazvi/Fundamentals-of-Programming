import random


class Repository:
    def __init__(self):
        self.matrix = []
        for i in range(7):
            self.matrix.append([0] * 7)

    def move(self,x,y,v): #put a X or O on the matrix
        if [x,y] in self.validity():
            self.matrix[x][y]=v


    def validity(self): # verifing the remaining valid moves and put them in possible_moves
       possible_moves=[]
       for i in range (1,7):
            for j in range (1,7):
                if self.matrix[i][j]==0:
                        possible_moves.append([i,j])
       return possible_moves

    def verify_win(self,i,j): #verifing if there exists 5 identical symbols in a row
        if (self.matrix[i][1]==self.matrix[i][2] and self.matrix[i][2]==self.matrix[i][3] and self.matrix[i][3]==self.matrix[i][4] and self.matrix[i][4]==self.matrix[i][5])==True or (self.matrix[i][2]==self.matrix[i][3] and self.matrix[i][3]==self.matrix[i][4] and self.matrix[i][4]==self.matrix[i][5] and self.matrix[i][5]==self.matrix[i][6])==True:
                return 1
        elif (self.matrix[1][j]==self.matrix[2][j] and self.matrix[2][j]==self.matrix[3][j] and self.matrix[3][j]==self.matrix[4][j] and self.matrix[4][j]==self.matrix[5][j])==True or (self.matrix[2][j]==self.matrix[3][j] and self.matrix[3][j]==self.matrix[4][j] and self.matrix[4][j]==self.matrix[5][j] and self.matrix[5][j]==self.matrix[6][j])==True:
                return 1
        elif ( self.matrix[1][1]==self.matrix[2][2] and self.matrix[2][2]==self.matrix[3][3] and self.matrix[3][3]==self.matrix[4][4] and self.matrix[4][4]==self.matrix[5][5])==True or ( self.matrix[2][2]==self.matrix[3][3] and self.matrix[3][3]==self.matrix[4][4] and self.matrix[4][4]==self.matrix[5][5] and self.matrix[5][5]==self.matrix[6][6])==True:
                return 1
        elif (self.matrix[5][0]==self.matrix[4][1] and self.matrix[4][1]==self.matrix[3][3] and self.matrix[3][3]==self.matrix[2][3] and self.matrix[2][3]==self.matrix[1][4])==True or (self.matrix[4][1]==self.matrix[3][3] and self.matrix[3][3]==self.matrix[2][3] and self.matrix[2][3]==self.matrix[1][4] and self.matrix[1][4]==self.matrix[0][5])==True:
                return 1
        else:
                return 0
    def computer_moves(self):
        return random.choice(self.validity())

    def get_table(self):
        return self.matrix

    def save_game(self, game):
        self.matrix.append(game)

    def load_game(self, index):
        return self.matrix[index]