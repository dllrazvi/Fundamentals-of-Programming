import random

from src.domain.domain import Complex

class Services:
    def __init__(self, repo):
        self.repo = repo
        self.undo_stack = []

    def add_complex_number(self, real, imag):
        assert type(real)==int and type(imag)==int, f"{real}/{imag} Not integers"
        number = Complex(real, imag)
        self.repo.add_complex_number(number)
        self.undo_stack.append(("add", number))

    def add_rand(self):
        number = Complex(random.randint(-10,10), random.randint(-10,10))
        self.repo.add_complex_number(number)
        self.undo_stack.append(("add", number))

    def get_complex_numbers(self):
        return self.repo.get_complex_numbers()

    def filter_complex_numbers(self, start, end):
        assert type(start)==int and type(end)==int,str(start)+'/'+str(end)+'not integers'
        assert start<=end,"Wrong indexes"
        assert start >= 0 and end < len(self.repo.complex_numbers), "Wrong indexes"
        return self.repo.filter_complex_numbers(start, end)

    def undo(self):
        if self.undo_stack:
            operation, number = self.undo_stack.pop()
            if operation == "add":
                self.repo.remove_complex_number(number)
