# Day 5 - Dictionaries and Sets
# Author: Vishvi
# Date: 2026-07-10
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Creating a Dictionary
# ─────────────────────────────────────

student = {
    'name':   'Vishvi',
    'age':    23,
    'city':   'Delhi',
    'course': 'Data Science',
    'gpa':    8.9
}

print(student)
print(student['name'])
print(student['gpa'])
print(len(student))

# ─────────────────────────────────────
# CONCEPT 2 - Adding, Updating, Removing
# ─────────────────────────────────────

student = {'name': 'Vishvi', 'age': 23}

student['city'] = 'Delhi'
student['age']  = 24
del student['city']
age = student.pop('age')
print(age)
print(student)

# ─────────────────────────────────────
# CONCEPT 3 - Dictionary Methods
# ─────────────────────────────────────

student = {'name': 'Vishvi', 'age': 23, 'city': 'Delhi'}

print(student.keys())
print(student.values())
print(student.items())

if 'name' in student:
    print('Name exists!')

print(student.get('salary', 'Not found'))

# ─────────────────────────────────────
# CONCEPT 4 - Looping through Dictionary
# ─────────────────────────────────────

marks = {
    'English': 85,
    'Maths':   92,
    'Science': 78,
    'Hindi':   88,
    'SST':     74
}

for subject in marks:
    print(subject)

for mark in marks.values():
    print(mark)

for subject, mark in marks.items():
    print(f'{subject}: {mark}')

# ─────────────────────────────────────
# CONCEPT 5 - Sets
# ─────────────────────────────────────

colors  = {'red', 'blue', 'green', 'red', 'blue'}
print(colors)

colors.add('yellow')
colors.remove('red')
print(colors)

print('blue' in colors)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)

# ─────────────────────────────────────
# CONCEPT 6 - Nested Dictionary
# ─────────────────────────────────────

students = {
    'Vishvi': {'age': 23, 'marks': 92, 'city': 'Delhi'},
    'Aditi':  {'age': 25, 'marks': 85, 'city': 'Mumbai'},
    'Rohan':  {'age': 22, 'marks': 78, 'city': 'Bangalore'}
}

print(students['Vishvi']['marks'])
print(students['Aditi']['city'])

for name, info in students.items():
    print(f"{name} scored {info['marks']} and lives in {info['city']}")

# ─────────────────────────────────────
# MINI PROJECT - Report Card with Dict
# ─────────────────────────────────────

print('===== REPORT CARD GENERATOR =====')

name     = input('Enter student name: ')
marks    = {}
subjects = ['English', 'Maths', 'Science', 'Hindi', 'SST']

for subject in subjects:
    marks[subject] = int(input(f'Enter {subject} marks: '))

total      = sum(marks.values())
percentage = round(total / 500 * 100, 2)
average    = round(total / len(marks), 2)

print(f"\n===== {name}'s Report Card =====")
for subject, mark in marks.items():
    grade = 'A' if mark >= 80 else 'B' if mark >= 60 else 'C' if mark >= 40 else 'F'
    print(f'  {subject:<10}: {mark}  ({grade})')

print(f'\nTotal      : {total}/500')
print(f'Percentage : {percentage}%')
print(f'Average    : {average}')
print(f"Result     : {'PASS' if total >= 204 else 'FAIL'}")
