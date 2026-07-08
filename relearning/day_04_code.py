# Day 4 - Lists and Tuples
# Author: Vishvi
# Date: 2026-07-08
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Creating a List
# ─────────────────────────────────────

fruits = ['apple', 'banana', 'mango', 'orange', 'grapes']

print(fruits)
print(fruits[0])     # first item
print(fruits[-1])    # last item
print(fruits[1:3])   # slice
print(len(fruits))   # how many items

# ─────────────────────────────────────
# CONCEPT 2 - Adding and Removing
# ─────────────────────────────────────

skills = ['Python', 'SQL', 'Excel']

skills.append('Machine Learning')
skills.insert(1, 'Pandas')
print(skills)

skills.remove('Excel')
skills.pop()
skills.pop(0)
print(skills)

# ─────────────────────────────────────
# CONCEPT 3 - List Operations
# ─────────────────────────────────────

numbers = [5, 2, 8, 1, 9, 3, 7]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# ─────────────────────────────────────
# CONCEPT 4 - Looping through a List
# ─────────────────────────────────────

students = ['Vishvi', 'Aditi', 'Rohan', 'Priya']

for student in students:
    print('Hello', student)

upper      = [s.upper() for s in students]
print(upper)

long_names = [s for s in students if len(s) > 5]
print(long_names)

# ─────────────────────────────────────
# CONCEPT 5 - Tuples
# ─────────────────────────────────────

coordinates = (28.6, 77.2)
colors      = ('red', 'green', 'blue')
person      = ('Vishvi', 23, 'Delhi')

print(coordinates)
print(colors[0])
print(person[1])

name, age, city = person
print(name)
print(age)
print(city)

print(type(coordinates))
print(type(colors))

# ─────────────────────────────────────
# CONCEPT 6 - Useful List Methods
# ─────────────────────────────────────

items = ['pen', 'book', 'pen', 'pencil', 'book', 'pen']

print(items.count('pen'))
print(items.index('book'))

items2 = ['ruler', 'eraser']
items.extend(items2)
print(items)

print('pen' in items)
print('bag' in items)

items_copy = items.copy()
items.clear()
print(items)
print(items_copy)

# ─────────────────────────────────────
# MINI PROJECT - Student Marks Manager
# ─────────────────────────────────────

students = []
marks    = []

print('===== STUDENT MARKS MANAGER =====')

for i in range(3):
    name  = input(f'Enter student {i+1} name: ')
    mark  = int(input(f'Enter {name} marks: '))
    students.append(name)
    marks.append(mark)

print('\n--- Results ---')
for i in range(len(students)):
    grade = 'Pass' if marks[i] >= 40 else 'Fail'
    print(f'{students[i]}: {marks[i]} marks - {grade}')

print(f'\nHighest marks: {max(marks)}')
print(f'Lowest marks:  {min(marks)}')
print(f'Class average: {sum(marks) // len(marks)}')
print(f'Topper: {students[marks.index(max(marks))]}')
