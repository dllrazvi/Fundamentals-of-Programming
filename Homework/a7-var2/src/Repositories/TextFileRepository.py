from src.domain.domain import Complex

class TextFileRepository:
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
        assert start>=0 and end<len(self.complex_numbers),"Wrong indexes"
        return self.complex_numbers[start:end]

    def remove_complex_number(self, number):
        self.complex_numbers.remove(number)
        self.save_complex_numbers()

    def load_complex_numbers(self):
        try:
            with open(self.filename, "r") as file:
                return [self.parse_complex_number(line) for line in file]
        except:
            return []

    def save_complex_numbers(self):
        with open(self.filename, "w") as file:
            for number in self.complex_numbers:
                file.write(self.format_complex_number(number) + "\n")

    def parse_complex_number(self, line):
        real, imag = line.strip().split(",")
        return Complex(int(real), int(imag))

    def format_complex_number(self, number):
        return f"{number.real},{number.imag}"
