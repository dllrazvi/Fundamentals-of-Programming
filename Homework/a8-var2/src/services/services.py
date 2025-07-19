from src.domain.domain import Student
from src.domain.domain import Grade
from src.domain.domain import Discipline
import random
import string
class Service:
    def __init__(self, repo):
        self.repo = repo

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.repo.add_student(student)

    def remove_student(self, student_id):
        self.repo.remove_student(student_id)

    def update_student_name(self, student_id, new_name):
        student = self.repo.get_student(student_id)
        student.name = new_name

    def list_students(self):
        return self.repo.get_all_students()

    def add_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.repo.add_discipline(discipline)

    def remove_discipline(self, discipline_id):
        self.repo.remove_discipline(discipline_id)

    def update_discipline_name(self, discipline_id, new_name):
        discipline = self.repo.get_discipline(discipline_id)
        discipline.name = new_name

    def list_disciplines(self):
        return self.repo.get_all_disciplines()

    def grade_student(self, discipline_id, student_id, grade_value):
        grade = Grade(discipline_id, student_id, grade_value)
        self.repo.add_grade(grade)

    def search_students(self, search_string):
        search_string = search_string.lower()
        matching_students = []
        for student in self.repo.get_all_students():
            if search_string in student.name.lower():
                matching_students.append(student)
        return matching_students

    def search_disciplines(self, search_string):
        search_string = search_string.lower()
        matching_disciplines = []
        for discipline in self.repo.get_all_disciplines():
            if search_string in discipline.name.lower():
                matching_disciplines.append(discipline)
        return matching_disciplines

    def get_failing_students(self):
        failing_students = []
        for student in self.repo.get_all_students():
            student_grades = self.repo.get_grades_for_student(student.student_id)
            student_average = 0
            total_disciplines = 0
            for grade in student_grades:
                student_average += grade.grade_value
                total_disciplines += 1
            if total_disciplines != 0:
                student_average /= total_disciplines
            if student_average < 5:
                failing_students.append(student)
        return failing_students

    def get_best_students(self):
        best_students = sorted(self.repo.get_all_students(), key=lambda x: self.get_student_average(x.student_id),
                               reverse=True)
        return best_students

    def get_best_disciplines(self):
        best_disciplines = sorted(self.repo.get_all_disciplines(),
                                  key=lambda x: self.get_discipline_average(x.discipline_id), reverse=True)
        return best_disciplines

    def get_student_average(self, student_id):
        student_grades = self.repo.get_grades_for_student(student_id)
        student_average = 0
        total_disciplines = 0
        for grade in student_grades:
            student_average += grade.grade_value
            total_disciplines += 1
        if total_disciplines != 0:
            student_average /= total_disciplines
        return student_average

    def get_discipline_average(self, discipline_id):
        discipline_grades = self.repo.get_grades_for_discipline(discipline_id)
        discipline_average = 0
        total_grades = 0
        for grade in discipline_grades:
            discipline_average += grade.grade_value
            total_grades += 1
        if total_grades != 0:
            discipline_average /= total_grades
        return discipline_average



