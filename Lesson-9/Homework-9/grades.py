import csv

filename = '/Users/macbook/Python/Lesson-9/Homework-9/grades.csv'
grades = []
with open(filename, 'rt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)

subject_grades = {}

for g in grades:
    subject = g['Subject']
    grade = g['Grade']

    if subject not in subject_grades:
        subject_grades[subject] = []

    subject_grades[subject].append(grade)

average_grades = []

for s, g in subject_grades.items():
    avg = sum(g)/len(g)
    average_grades.append({"Subject": s, "Average grade": avg})

with open('average_grades.csv', 'w') as file:
    fieldnames = ["Subject", "Average grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(average_grades)




