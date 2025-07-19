import pickle

class BinaryFileRepository:
    def __init__(self, filename):
        self.filename = filename
        self.complex_numbers = self.load_complex_numbers()

    def add_complex_number(self, number):
        self.complex_numbers.append(number)
        self.save_complex_numbers()

    def get_complex_numbers(self):
        return self.complex_numbers

    def filter_complex_numbers(self, start, end):
        assert type(start) == int and type(end) == int, str(start) + '/' + str(end) + 'not integers'
        assert start <= end, "Wrong indexes"
        assert start >= 0 and end < len(self.complex_numbers), "Wrong indexes"
        return self.complex_numbers[start:end]

    def remove_complex_number(self, number):
        self.complex_numbers.remove(number)
        self.save_complex_numbers()

    def load_complex_numbers(self):
        try:
            with open(self.filename, "rb") as file:
                return pickle.load(file)
        except:
            return []

    def save_complex_numbers(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.complex_numbers, file)
