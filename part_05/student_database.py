def print_student(dictionary: dict, name: str):

    if name in dictionary:
        print(f"{name}: ")

        tuple_number = len(dictionary[name])
        if tuple_number != 0:
            print(f" {tuple_number} completed courses:")

        if dictionary[name] == ():
            print(f" no completed courses")
        else:
            add = 0
            i = 0
            for course_name, grade in dictionary[name]:
                print(f"  {course_name} {grade}")
                add += grade
                i += 1
            print(f" average grade {add / i:.1f}")
    else:
        print(f"{name}: no such person in the database")

def add_student(dictionary: dict, name: str):
    if name not in dictionary:
        dictionary[name] = ()

def add_course(dictionary: dict, name: str, course: tuple):

    if course[1] == 0:
        return

    new_courses = ()
    found = False
    for course_name, grade in dictionary[name]:
        if course_name == course[0]:
            found = True
            if course[1] > grade:
                new_courses += (course,)
            else:
                new_courses += ((course_name, grade),)
        else:
            new_courses += ((course_name, grade),)
    
    if not found:
        new_courses += (course,)

    dictionary[name] = new_courses

def summary(students: dict):
    most = -1
    most_courses_name = ""
    best_average = -1
    best_average_name = ""

    for name in students:
        courses = students[name]

        if len(courses) > most:
            most = len(courses)
            most_courses_name = name

        if len(courses) > 0:
            total = 0
            for course, grade in courses:
                total += grade
            average = total / len(courses)

            if average > best_average:
                best_average = average
                best_average_name = name

    print(f"students {len(students)}")
    print(f"most courses completed {most} {most_courses_name}")
    print(f"best average grade {best_average:.1f} {best_average_name}")


# Write your solution here

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)