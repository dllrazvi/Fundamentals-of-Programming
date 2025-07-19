import random
import string
from src.domain.domain import Student, Grade, Discipline
class Generate():
    def __init__(self,student,grade,discipline):
        self.student= Student
        self.grade= Grade
    def generate_random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def generate_random_student(self):
        student_id = random.randint(1, 10000)
        name = self.generate_random_string(10)
        return Student(Student.student_id, Student.name)

    def generate_random_discipline(self):
        discipline_id = random.randint(1, 10000)
        name = self.generate_random_string(10)
        return Discipline(Discipline.discipline_id, Discipline.name)

    def generate_random_grade(self):
        student_id = random.randint(1, 10000)
        discipline_id = random.randint(1, 10000)
        grade = random.randint(1, 10)
        return Grade(Student.student_id, Discipline.discipline_id, Grade.grade)

    def generate_random_data(self,num_students, num_disciplines, num_grades):
        students = [self.generate_random_student() for _ in range(num_students)]
        disciplines = [self.generate_random_discipline() for _ in range(num_disciplines)]
        grades = [self.generate_random_grade() for _ in range(num_grades)]
        return students, disciplines, grades
