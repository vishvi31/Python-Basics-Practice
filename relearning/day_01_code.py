# Day 1 - Variables, Print, Input and Math
# Author: Vishvi
# Date: 2026-07-04
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CELL 1 - Print statements
# ─────────────────────────────────────

print('Hello Vishvi')
print('What are you doing?')
print('I enjoy coding!')

# ─────────────────────────────────────
# CELL 2 - Variables and Data Types
# ─────────────────────────────────────

my_name     = 'Vishvi'  # String
my_age      = 18        # Integer
my_gpa      = 8.9       # Float
is_learning = True      # Boolean

print(my_name,     type(my_name))
print(my_age,      type(my_age))
print(my_gpa,      type(my_gpa))
print(is_learning, type(is_learning))

# ─────────────────────────────────────
# CELL 3 - Math Operations with Input
# ─────────────────────────────────────

a = int(input('Write your first number: '))
b = int(input('Write your second number: '))

print(a - b)   # Subtraction
print(a + b)   # Addition
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a ** b)  # Power
print(a % b)   # Remainder (modulo)

# ─────────────────────────────────────
# CELL 4 - RESULT CARD PROGRAM
# (Vishvi's own project - built on Day 1!)
# ─────────────────────────────────────

print('********************************** RESULT OUT **************************************')

name = input('Write your name: ')
age  = input('Write your age: ')

print('*** Now write your marks ***')
English = int(input('English: '))
Maths   = int(input('Maths: '))
Science = int(input('Science: '))
SST     = int(input('SST: '))
Hindi   = int(input('Hindi: '))

Total      = English + Maths + Science + SST + Hindi
Percentage = int(Total / 500 * 100)

print(f'Your total marks are: ', Total)
print(f'Your percentage is: ', Percentage)

if Total >= 204:
    print(f'Congratulations {name}! You are passed and promoted to the next class!')
else:
    print(f'Sadly {name}, you are failed and not promoted to the next class.')
