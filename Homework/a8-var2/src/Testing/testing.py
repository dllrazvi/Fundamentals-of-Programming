import unittest
from src.services.services import Service
from src.repository.repository import Repository
from src.domain.domain import Student

class TestService(unittest.TestCase):
    def setUp(self):
        self.repo = Repository()
        self.service = Service(self.repo)

    def test_add_student(self):
        student = Student(1, "John Doe")
        self.service.add_student(student)
        result = self.service.get_student(1)
        self.assertEqual(result, student)

    def test_add_student_duplicate(self):
        student = Student(1, "John Doe")
        self.service.add_student(student)
        with self.assertRaises(StudentAlreadyExistsError):
            self.service.add_student(student)

    def test_get_student_not_found(self):
        with self.assertRaises(StudentNotFoundError):
            self.service.get_student(1)

if __name__ == '__main__':
    unittest.main()
