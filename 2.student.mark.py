class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.students.append(student)
        print(f"Successfully added {n} students")

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.courses.append(course)
        print(f"Successfully added {n} courses")

    def input_marks(self):
        course_id = input("Enter course id: ")
        for course in self.courses:
            if course.id == course_id:
                for student in self.students:
                    mark = int(input(f"Enter mark for student {student.id}: "))
                    course.marks[student.id] = mark
                print(f"Successfully added marks for course {course.name}")
                return
        print("Course not found")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, Date of Birth: {student.dob}")

    def show_student_marks(self):
        course_id = input("Enter course id: ")
        for course in self.courses:
            if course.id == course_id:
                print(f"List of marks for course {course.name}")
                for student, mark in course.marks.items():
                    print(f"Student ID: {student}, Mark: {mark}")
                return
        print("Course not found")
StudentMarkManagementSystem=StudentMarkManagementSystem()
while True:
            print("Menu:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks for a given course")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                StudentMarkManagementSystem.input_students()
            elif choice == 2:
                StudentMarkManagementSystem.input_courses()
            elif choice == 3:
                StudentMarkManagementSystem.input_marks()
            elif choice == 4:
                StudentMarkManagementSystem.list_courses()
            elif choice == 5:
                StudentMarkManagementSystem.list_students()
            elif choice == 6:
                StudentMarkManagementSystem.show_student_marks()
            elif choice == 7:
                break
            else:
                print("Invalid choice, please try again")
