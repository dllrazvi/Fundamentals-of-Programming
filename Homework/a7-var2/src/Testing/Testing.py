import unittest
import random
from src.domain.domain import Complex
from src.Repositories.MemoryRepository import MemoryRepository
from src.services.services import Services

class TestServices(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepository()
        self.services = Services(self.repo)

    def test_add_complex_number(self):
        self.services.add_complex_number(1, 2)
        self.assertEqual(len(self.repo.complex_numbers), 1)
        self.assertEqual(self.repo.complex_numbers[0], Complex(1, 2))

    def test_add_rand(self):
        self.services.add_rand()
        self.assertEqual(len(self.repo.complex_numbers), 1)
        self.assertIsInstance(self.repo.complex_numbers[0], Complex)

    def test_get_complex_numbers(self):
        self.services.add_complex_number(1, 2)
        self.services.add_complex_number(3, 4)
        self.assertEqual(self.services.get_complex_numbers(), [Complex(1, 2)],Complex(3, 4))

    def test_filter_complex_numbers(self):
        self.services.add_complex_number(1, 2)
        self.services.add_complex_number(3, 4)
        self.services.add_complex_number(5, 6)
        self.assertEqual(self.services.filter_complex_numbers(0, 1), [Complex(1, 2), Complex(3, 4)])

    def test_undo(self):
        self.services.add_complex_number(1, 2)
        self.services.undo()
        self.assertEqual(len(self.repo.complex_numbers), 0)

if __name__ == '__main__':
    unittest.main()
