import random

from src.domain.domain import Complex

class MemoryRepository:
    def __init__(self):
        self.complex_numbers = []

    def add_complex_number(self, number:list):
        self.complex_numbers.append(number)

    def get_complex_numbers(self):
        return self.complex_numbers

    def filter_complex_numbers(self, start, end):
        assert start >= 0 and end < len(self.complex_numbers), "Wrong indexes"
        assert start <= end, "Wrong indexes"
        return self.complex_numbers[start:end]

    def add_rand(self):
        self.complex_numbers_append()
    def remove_complex_number(self, number):
        self.complex_numbers.remove(number)
