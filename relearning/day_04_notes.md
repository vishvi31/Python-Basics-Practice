# Day 4 - What I Learned

Author: Vishvi
Date: 2026-07-08

---

## Concepts Practiced

| Concept | What it does | Example |
|---|---|---|
| list | Stores multiple values | fruits = ['apple', 'mango'] |
| list[0] | Get first item | fruits[0] = 'apple' |
| list[-1] | Get last item | fruits[-1] = 'grapes' |
| list[1:3] | Get slice | fruits[1:3] = ['banana','mango'] |
| append() | Add to end | skills.append('ML') |
| insert() | Add at position | skills.insert(1,'Pandas') |
| remove() | Remove by value | skills.remove('Excel') |
| pop() | Remove last | skills.pop() |
| sort() | Sort the list | numbers.sort() |
| reverse() | Reverse the list | numbers.reverse() |
| count() | Count occurrences | items.count('pen') |
| index() | Find position | items.index('book') |
| extend() | Join two lists | items.extend(items2) |
| in | Check if exists | 'pen' in items |
| copy() | Make a copy | items_copy = items.copy() |
| clear() | Empty the list | items.clear() |
| tuple | Like list but unchangeable | person = ('Vishvi', 23) |
| unpacking | Split tuple into variables | name, age = person |

---

## List vs Tuple

| | List | Tuple |
|---|---|---|
| Symbol | [ ] | ( ) |
| Can change? | YES | NO |
| Use when | Data changes | Data is fixed |
| Example | Shopping list | GPS coordinates |

---

## Why Loops + Lists Together?

Without loop - works for fixed number only:
English = int(input('English: '))
Maths   = int(input('Maths: '))

With loop + list - works for ANY number:
for i in range(3):   change 3 to anything!
    students.append(input('Name: '))

---

## Tomorrow - Day 5

Topic: Dictionaries and Sets

---

Built by Vishvi - github.com/vishvi31
