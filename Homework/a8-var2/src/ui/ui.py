from src.repository.repository import Repository
from src.domain.domain import Student
from src.domain.domain import Grade
from src.domain.domain import Discipline
from src.services.services import Service
class UI:
    def __init__(self, service):
        self.service = service



    def display_menu(self):
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. List students")
        print("5. Add discipline")
        print("6. Remove discipline")
        print("7. Update discipline")
        print("8. List disciplines")
        print("9. Grade student")
        print("10. Search students")
        print("11. Search disciplines")
        print("12. Failing students")
        print("13. Best students")
        print("14. Best disciplines")
        print("15. Exit")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                self.service.add_student(student_id, name)
                print("Student added successfully!")
            elif choice == "2":
                student_id = input("Enter student ID: ")
                self.service.remove_student(student_id)
                print("Student removed successfully!")
            elif choice == "3":
                student_id = input("Enter student ID: ")
                new_name = input("Enter new name: ")
                self.service.update_student_name(student_id, new_name)
                print("Student updated successfully!")
            elif choice == "4":
                students = self.service.list_students()
                for student in students:
                    print(student)
            elif choice == "5":
                discipline_id = input("Enter discipline ID: ")
                name = input("Enter discipline name: ")
                self.service.add_discipline(discipline_id, name)
                print("Discipline added successfully!")
            elif choice == "6":
                discipline_id = input("Enter discipline ID: ")
                self.service.remove_discipline(discipline_id)
                print("Discipline removed successfully!")
            elif choice == "7":
                discipline_id = input("Enter discipline ID: ")
                new_name = input("Enter new name: ")
                self.service.update_discipline_name(discipline_id, new_name)
                print("Discipline updated successfully!")
            elif choice == "8":
                disciplines = self.service.list_disciplines()
                for discipline in disciplines:
                    print(discipline)
            elif choice == "9":
                discipline_id = input("Enter discipline ID: ")
                student_id = input("Enter student ID: ")
                grade_value = input("Enter grade value: ")
                self.service.grade_student(discipline_id, student_id, grade_value)
                print("Grade added successfully!")
            elif choice == "10":
                search_string = input("Enter search string: ")
                self.service.search_students(search_string)
            elif choice == "11":
                search_string = input("Enter search string: ")
                self.service.search_disciplines(search_string)
            elif choice == "12":
                self.service.get_failing_students()
            elif choice == "13":
                self.service.get_best_students()
            elif choice == "14":
                self.service.get_best_disciplines()
            elif choice == "15":
                self.exit()
            else:
                print("Invalid choice. Please enter a valid choice.")

if __name__=="__main__":
    repo= Repository()
    services= Service(repo)
    ui= UI(services)
    ui.start()

