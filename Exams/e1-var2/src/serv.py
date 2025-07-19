from repo import Repository

class Service: # redirecting instructions to the repo file
    def __init__(self):
        self.repository = Repository()

    def move(self, x, y, v):
        self.repository.move(x, y, v)

    def validity(self):
        return self.repository.validity()
    def print_table(self):
        return self.repository.get_table()
    def verify_win(self, i,j):
        return self.repository.verify_win(i,j)
    def save_game(self, game):
        self.repository.save_game(game)
    def computer_moves(self):
        self.repository.computer_moves()
    def load_game(self, index):
        return self.repository.load_game(index)
