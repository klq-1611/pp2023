students = []
courses = []

def input_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = (id, name, dob)
        students.append(student)
    print(f"Successfully added {n} students")

def input_courses():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        course = (id, name, {})
        courses.append(course)
    print(f"Successfully added {n} courses")

def input_marks():
    course_id = input("Enter course id: ")
    for course in courses:
        if course[0] == course_id:
            for student in students:
                mark = int(input(f"Enter mark for student {student[0]}: "))
                course[2][student[0]] = mark
            print(f"Successfully added marks for course {course[1]}")
            return
    print("Course not found")

def list_courses():
    print("List of courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks():
    course_id = input("Enter course id: ")
    for course in courses:
        if course[0] == course_id:
            print(f"List of marks for course {course[1]}")
            for student, mark in course[2].items():
                print(f"Student ID: {student}, Mark: {mark}")
            return
    print("Course not found")

def student_mark_management_system():
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
            input_students()
        elif choice == 2:
            input_courses()
        elif choice == 3:
            input_marks()
        elif choice == 4:
            list_courses()
        elif choice == 5:
            list_students()
        elif choice == 6:
            show_student_marks()
        elif choice == 7:
            break
        else:
            print("Invalid choice, please try again")

student_mark_management_system()
