class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __str__(self):
        return f"{self.student_id} - {self.name}"

    def update_name(self, new_name):
        self.name = new_name


class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self.discipline_id = discipline_id
        self.student_id = student_id
        self.grade_value = grade_value

    def __str__(self):
        return f"{self.discipline_id} - {self.student_id} - {self.grade_value}"

class Discipline:
    def __init__(self, discipline_id, name):
        self.discipline_id = discipline_id
        self.name = name

    def __str__(self):
        return f"{self.discipline_id} - {self.name}"
