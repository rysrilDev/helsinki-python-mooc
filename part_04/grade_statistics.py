def points_and_exercises():
    student_points = []
    student_exercises = []
    while True:
        exam_and_exercise_points = (input("Exam points and exercises completed: "))

        if exam_and_exercise_points == "":
            break

        parts = exam_and_exercise_points.split()
        points = int(parts[0])
        exercises = int(parts[1])
        student_points.append(points)
        student_exercises.append(exercises)

    print("Statistics: ")
    return student_points, student_exercises

def statistics(stu_points, stu_exercises):
    # for n in stu_points:
        # if n < 10:
        #    index_num = stu_points.index(n)

        #    stu_points.remove(n)
        #    stu_exercises.remove(stu_exercises[index_num])
    total = []
    for numbers in range(0, len(stu_points)):
        total.append(stu_points[numbers] + (stu_exercises[numbers] // 10))

    return total

def grading(stu_points, total_points):
    grade_list = []
    for i in range(0, (len(total_points))):

        if stu_points[i] < 10:
            grade_list.append(0)
        elif total_points[i] <= 14:
            grade_list.append(0)
        elif total_points[i] <= 17:
            grade_list.append(1)
        elif total_points[i] <= 20:
            grade_list.append(2)
        elif total_points[i] <= 23:
            grade_list.append(3)
        elif total_points[i] <= 27:
            grade_list.append(4)
        else:
            grade_list.append(5)

    return grade_list

def grade_table(total_points, grade_list):
    all_sum = 0
    passing_students = len(grade_list) - grade_list.count(0)
    for i in total_points:
        all_sum += i

    print(f"Points average: {all_sum / len(grade_list):.1f}")
    print(f"Pass percentage: {passing_students / len(grade_list) * 100:.1f}")
    print("Grade distribution:")
    for number in range(5, -1, -1):
        stars = "*" * grade_list.count(number)
        print(f"  {number}: {stars}")
# Write your solution here

def main():
    stu_points, stu_exercises = points_and_exercises()
    total_points = statistics(stu_points, stu_exercises)
    grade_list = grading(stu_points, total_points)
    grade_table(total_points, grade_list)

main()