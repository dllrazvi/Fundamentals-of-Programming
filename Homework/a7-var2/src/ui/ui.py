from src.Repositories.BinaryFileRepository import BinaryFileRepository
from src.Repositories.TextFileRepository import TextFileRepository
from src.Repositories.MemoryRepository import MemoryRepository
from src.services.services import Services
import random
class UI:
    def __init__(self, services):
        self.services = services
        self.generate_random_numbers()

    def generate_random_numbers(self):
        for i in range(0,9):
            real = random.randint(-10, 10)
            imag = random.randint(-10, 10)
            self.services.add_complex_number(real, imag)

    def start(self):
        while True:
            print("1. Add a complex number")
            print("2. Display the list of complex numbers")
            print("3. Filter the list of complex numbers")
            print("4. Undo the last operation")
            print("5. Exit")
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.add_complex_number()
                elif choice == "2":
                    self.display_complex_numbers()
                elif choice == "3":
                    self.filter_complex_numbers()
                elif choice == "4":
                    self.undo()
                elif choice == "5":
                    break
            except NameError:
                print("The option chosen is wrong")

    def add_complex_number(self):
        real = int(input("Enter the real part: "))
        imag = int(input("Enter the imaginary part: "))
        self.services.add_complex_number(real, imag)

    def display_complex_numbers(self):
        complex_numbers = self.services.get_complex_numbers()
        for number in complex_numbers:
            print(number)

    def filter_complex_numbers(self):
        start = int(input("Enter the start index: "))
        end = int(input("Enter the end index: "))
        filtered_numbers = self.services.filter_complex_numbers(start, end)
        for number in filtered_numbers:
            print(number)

    def undo(self):
        self.services.undo()

if __name__ == "__main__":
    print("Choose the repository wanted: ")
    print("1 = Memory")
    print("2 = Binary")
    print("3 = TextFile")
    option=input("The option: ")
    assert option=='1' or option=='2' or option=='3',"Wrong option"
    if option == '1':
            repo = MemoryRepository()
    elif option == '2':
            repo= BinaryFileRepository("complex_numbers.bin")
    elif option == '3':
            repo= TextFileRepository("complex_numbers.txt")
    services = Services(repo)
    ui = UI(services)
    ui.start()


