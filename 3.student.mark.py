import curses
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

    def compute_gpa(self, marks):
        grade_scale = {
            20: 'A+',
            18: 'A',
            16: 'B+',
            14: 'B',
            12: 'C+',
            10: 'C',
            8: 'D+',
            6: 'D',
            0: 'F'
        }
        total_credits = 0
        total_grade_points = 0
        for course, mark in marks.items():
            for c in self.courses:
                if c.id == course:
                    credits = len(c.name)
                    grade_point = 0
                    for grade, grade_letter in grade_scale.items():
                        if mark >= grade:
                            grade_point = credits * grade
                            total_grade_points += grade_point
                            total_credits += credits
                            break
                    break
        gpa = total_grade_points / total_credits
        return round(gpa, 2)

    def show_student_gpa(self):
        student_id = input("Enter student id: ")
        for student in self.students:
            if student.id == student_id:
                marks = {}
                for course in self.courses:
                    if student_id in course.marks:
                        marks[course.id] = course.marks[student_id]
                gpa = self.compute_gpa(marks)
                print(f"Student ID: {student.id}, GPA: {gpa}")
                return
        print("Student not found")

    def show_course_gpa(self):
        course_id = input("Enter course id: ")
        for course in self.courses:
            if course.id == course_id:
                marks = {}
                for student in self.students:
                    if course_id in student.marks:
                        marks[course.id] = student.marks[course_id]
                gpa = self.compute_gpa(marks)
                print(f"Course ID: {course.id}, GPA: {gpa}")
                return
        print("Course not found")

    def show_gpa(self):
        print("1. Show student GPA")
        print("2. Show course GPA")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.show_student_gpa()
        elif choice == '2':
            self.show_course_gpa()
        else:
            print("Invalid choice")

    def show_menu(self):
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks")
        print("7. Show GPA")
        print("8. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '7':
                self.show_gpa()
            elif choice == '8':
                break
            else:
                print("Invalid choice")

if __name__ == '__main__':
    smms = StudentMarkManagementSystem()
    smms.run()

