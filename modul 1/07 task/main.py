grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = []
for i in grades:
    x = sum(i)/len(i)
    average_grades.append(x)

students = sorted(list(students))
average_students_grades = dict(zip(students, average_grades))

print(average_students_grades)
