# Error Handling in Python

Author: Vishvi
Date: 2026-06-08

---

## What is Error Handling?

When your code hits a problem, Python throws an error
and stops completely. Error handling lets you catch
that problem and decide what to do instead of crashing.

---

## Code

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero!')

# Catching multiple errors
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

# try-except-else-finally
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('File not found:', filename)
    except PermissionError:
        print('No permission to read:', filename)
    else:
        print('File read successfully!')
        return content
    finally:
        print('read_file() finished.')

read_file('notes.txt')
read_file('missing.txt')

# Raising custom errors
def set_age(age):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if age < 0 or age > 120:
        raise ValueError('Age must be between 0 and 120')
    return age

try:
    print(set_age(25))
    print(set_age(-5))
except ValueError as e:
    print('ValueError:', e)

# Custom exception class
class DataScienceError(Exception):
    pass

def load_dataset(path):
    if not path.endswith('.csv'):
        raise DataScienceError('Only CSV files are supported!')
    return 'Dataset loaded from: ' + path

try:
    print(load_dataset('data.csv'))
    print(load_dataset('data.xlsx'))
except DataScienceError as e:
    print('DataScienceError:', e)
```

---

## Key Terms

| Block | When it runs |
|---|---|
| try | The code you want to run |
| except | Runs if there is an error |
| else | Runs only if NO error occurred |
| finally | Always runs no matter what |

---

## Connection to Data Science

- Handling missing CSV files gracefully
- Catching API errors in data collection
- Validating user input in Flask web apps
- Writing robust ML pipelines that dont crash

---

Built by Vishvi - github.com/vishvi31
