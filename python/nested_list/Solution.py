if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
    students.sort(key = lambda x: x[0])
    min_grade = min(students, key = lambda x: x[1])
    students = [x for x in students if x[1] > min_grade[1]]
    min_grade = min(students, key = lambda x: x[1])
    for student in students:
        if student[1] == min_grade[1]:
            print(student[0])