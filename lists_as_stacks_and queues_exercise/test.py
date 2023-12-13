number_of_students = int(input())
students = {}

for student in range(number_of_students):
    current_name, current_grade = input().split()
    if current_name not in students:
        students[current_name] = []
    students[current_name].append(float(current_grade))

for name, grade in students.items():
    print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grade)} (avg: {sum(grade) / len(grade):.2f})")
