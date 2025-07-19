from typing import List
from src.domain.domain import Student, Discipline, Grade

class Repository:
    def __init__(self):
        self.students = {}
        self.disciplines = {}
        self.grades = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise StudentAlreadyExistsError(student.student_id)
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        del self.students[student_id]
        for grade in self.grades.values():
            if grade.student_id == student_id:
                del self.grades[grade.grade_id]

    def update_student_name(self, student_id, new_name):
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        student = self.students[student_id]
        student.name = new_name

    def get_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError(student_id)
        return self.students[student_id]

    def get_all_students(self):
        return list(self.students.values())

    def add_discipline(self, discipline):
        if discipline.discipline_id in self.disciplines:
            raise DisciplineAlreadyExistsError(discipline.discipline_id)
        self.disciplines[discipline.discipline_id] = discipline

    def remove_discipline(self, discipline_id):
        if discipline_id not in self.disciplines:
            raise DisciplineNotFoundError(discipline_id)
        del self.disciplines[discipline_id]
        for grade in self.grades.values():
            if grade.discipline_id == discipline_id:
                del self.grades[grade.grade_id]

    def update_discipline_name(self, discipline_id, new_name):
        if discipline_id not in self.disciplines:
            raise DisciplineNotFoundError(discipline_id)
        discipline = self.disciplines[discipline_id]
        discipline.name = new_name

    def get_discipline(self, discipline_id):
        if discipline_id not in self.disciplines:
            raise DisciplineNotFoundError(discipline_id)
        return self.disciplines[discipline_id]

    def get_all_disciplines(self):
        return list(self.disciplines.values())

    def add_grade(self, Grade):
        if Grade.grade_id in self.grades:
            raise GradeAlreadyExistsError(Grade.grade_id)
        self.grades[Grade.grade_id] = Grade

    def remove_grade(self, grade_id):
        if grade_id not in self.grades:
            raise GradeNotFoundError(grade_id)
        del self.grades[grade_id]

    def get_grade(self, grade_id):
        if grade_id not in self.grades:
            raise GradeNotFoundError(grade_id)
        return self.grades[grade_id]

    def get_grades_for_student(self, student_id):
        student_grades = []
        for grade in self.grades.values():
            if grade.student_id == student_id:
                student_grades.append(grade)
        return student_grades

    def get_grades_for_discipline(self, discipline_id):
        discipline_grades = []
        for grade in self.grades.values():
            if grade.discipline_id == discipline_id:
                discipline_grades.append(grade)
class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        self.student_id = student_id
    def __str__(self):
        return f"Student with id {self.student_id} not found"

class DisciplineNotFoundError(Exception):
    def __init__(self, discipline_id):
        self.discipline_id = discipline_id
    def __str__(self):
        return f"Discipline with id {self.discipline_id} not found"

class GradeNotFoundError(Exception):
    def __init__(self, grade_id):
        self.grade_id = grade_id
    def __str__(self):
        return f"Grade with id {self.grade_id} not found"

class StudentAlreadyExistsError(Exception):
    def __init__(self, student_id):
        self.student_id = student_id
    def __str__(self):
        return f"Student with id {self.student_id} already exists"

class DisciplineAlreadyExistsError(Exception):
    def __init__(self, discipline_id):
        self.discipline_id = discipline_id
    def __str__(self):
        return f"Discipline with id {self.discipline_id} already exists"

class GradeAlreadyExistsError(Exception):
    def __init__(self, grade_id):
        self.grade_id = grade_id
    def __str__(self):
        return f"Grade with id {self.grade_id} already exists"


