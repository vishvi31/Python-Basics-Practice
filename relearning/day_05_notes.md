# Day 5 - What I Learned

Author: Vishvi
Date: 2026-07-10

---

## Concepts Practiced

| Concept | What it does | Example |
|---|---|---|
| dictionary | Stores key-value pairs | student = {'name': 'Vishvi'} |
| dict[key] | Get value by key | student['name'] |
| dict[key] = val | Add or update | student['city'] = 'Delhi' |
| del dict[key] | Remove a key | del student['city'] |
| pop() | Remove and return | student.pop('age') |
| keys() | All keys | student.keys() |
| values() | All values | student.values() |
| items() | All key-value pairs | student.items() |
| get() | Safe access with default | student.get('x', 'Not found') |
| in | Check if key exists | 'name' in student |
| set | Unique values only | colors = {'red', 'blue'} |
| add() | Add to set | colors.add('yellow') |
| remove() | Remove from set | colors.remove('red') |
| | Union - all items | a | b |
| & | Intersection - common | a & b |
| - | Difference | a - b |
| nested dict | Dict inside dict | students['Vishvi']['marks'] |

---

## List vs Dictionary vs Set

| | List | Dictionary | Set |
|---|---|---|---|
| Symbol | [ ] | { : } | { } |
| Stores | Values | Key-Value pairs | Unique values |
| Access by | Index [0] | Key ['name'] | Cannot access by index |
| Duplicates | Yes | No duplicate keys | No duplicates |
| Use when | Ordered items | Label your data | Remove duplicates |

---

## My Progress - Day 1 vs Day 5

Day 1 Result Card - used separate variables:
English = int(input('English: '))
Maths   = int(input('Maths: '))

Day 5 Report Card - used dictionary and loop:
for subject in subjects:
    marks[subject] = int(input(f'Enter {subject} marks: '))

Same result. Much cleaner code. That is growth!

---

## Tomorrow - Day 6

Topic: Functions

---

Built by Vishvi - github.com/vishvi31
