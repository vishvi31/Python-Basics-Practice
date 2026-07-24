# Day 9 - Error Handling
# Author: Vishvi
# Date: 2026-07-24

# CONCEPT 1 - Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')

# CONCEPT 2 - Multiple exceptions
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero'
    except TypeError:
        return 'Error: Invalid input type'

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, 'a'))

# CONCEPT 3 - try/except/else/finally
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f'File not found: {filename}')
    except PermissionError:
        print('No permission!')
    else:
        print('File read successfully!')
        return content
    finally:
        print('read_file() finished.')

read_file('notes.txt')
read_file('missing.txt')

# CONCEPT 4 - Custom errors
def set_age(age):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if age < 0 or age > 120:
        raise ValueError('Age must be 0-120')
    return age

try:
    print(set_age(25))
    print(set_age(-5))
except ValueError as e:
    print('ValueError:', e)

# CONCEPT 5 - Custom Exception Class
class DataScienceError(Exception):
    pass

def load_dataset(path):
    if not path.endswith('.csv'):
        raise DataScienceError('Only CSV files supported!')
    return f'Loaded: {path}'

try:
    print(load_dataset('data.csv'))
    print(load_dataset('data.xlsx'))
except DataScienceError as e:
    print('DataScienceError:', e)
