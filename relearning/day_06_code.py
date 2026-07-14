# Day 6 - Functions
# Author: Vishvi
# Date: 2026-07-14
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Basic Function
# ─────────────────────────────────────

def greet():
    print('Hello!')
    print('Welcome to Python!')

greet()
greet()
greet()

# ─────────────────────────────────────
# CONCEPT 2 - Function with Parameters
# ─────────────────────────────────────

def greet(name):
    print(f'Hello {name}!')
    print(f'Welcome to Python, {name}!')

greet('Vishvi')
greet('Aditi')
greet('Rohan')

# ─────────────────────────────────────
# CONCEPT 3 - Function with Return
# ─────────────────────────────────────

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(n):
    return n ** 2

print(add(5, 3))
print(multiply(4, 6))
print(square(7))
print(add(10, 20) + multiply(2, 3))

# ─────────────────────────────────────
# CONCEPT 4 - Default Parameters
# ─────────────────────────────────────

def greet(name, message='Good morning'):
    print(f'{message}, {name}!')

greet('Vishvi')
greet('Aditi', 'Good evening')
greet('Rohan', 'Happy birthday')

# ─────────────────────────────────────
# CONCEPT 5 - Multiple Return Values
# ─────────────────────────────────────

def calculate(a, b):
    total      = a + b
    difference = a - b
    product    = a * b
    quotient   = a / b
    return total, difference, product, quotient

t, d, p, q = calculate(10, 2)
print('Total:     ', t)
print('Difference:', d)
print('Product:   ', p)
print('Quotient:  ', q)

# ─────────────────────────────────────
# CONCEPT 6 - Functions calling Functions
# ─────────────────────────────────────

def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

def get_result(marks):
    return 'PASS' if marks >= 40 else 'FAIL'

def print_report(name, marks):
    grade  = get_grade(marks)
    result = get_result(marks)
    print(f'{name}: {marks} marks | Grade: {grade} | {result}')

print_report('Vishvi', 92)
print_report('Aditi',  75)
print_report('Rohan',  35)

# ─────────────────────────────────────
# MINI PROJECT - Calculator
# ─────────────────────────────────────

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return 'Error! Cannot divide by zero'
    return round(a / b, 2)

def calculator():
    print('===== PYTHON CALCULATOR =====')
    a = float(input('Enter first number:  '))
    b = float(input('Enter second number: '))
    print('\n1. Add  2. Subtract  3. Multiply  4. Divide')
    choice = input('Your choice: ')
    if   choice == '1': print('Answer:', add(a, b))
    elif choice == '2': print('Answer:', subtract(a, b))
    elif choice == '3': print('Answer:', multiply(a, b))
    elif choice == '4': print('Answer:', divide(a, b))
    else: print('Invalid choice!')

calculator()
