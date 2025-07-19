class Domain:
    def __init__(self):
        self.matrix = [[0] * 6 for i in range(6)]
        self.turn = 1

    def play_move(self, x, y, v):
        if self.matrix[x][y] == 0:
            self.matrix[x][y] = v
            self.turn = 3 - self.turn
            return True
        else:
            return False

    def get_matrix(self):
        return self.matrix

    def get_turn(self):
        return self.turn

    def print_matrix(self):
        print(self.get_matrix())