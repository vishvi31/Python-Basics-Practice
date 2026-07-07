# Day 2 - If / Elif / Else Conditions
# Author: Vishvi
# Date: 2026-07-07
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Basic If/Else
# ─────────────────────────────────────

age = 18

if age >= 18:
    print('You are an adult')
else:
    print('You are a minor')

# ─────────────────────────────────────
# CONCEPT 2 - If / Elif / Else
# ─────────────────────────────────────

marks = 75

if marks >= 90:
    print('Grade A')
elif marks >= 75:
    print('Grade B')
elif marks >= 60:
    print('Grade C')
elif marks >= 40:
    print('Grade D')
else:
    print('Grade F - Failed')

# ─────────────────────────────────────
# CONCEPT 3 - Conditions with input()
# ─────────────────────────────────────

number = int(input('Enter a number: '))

if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('Zero')

# ─────────────────────────────────────
# CONCEPT 4 - and / or / not
# ─────────────────────────────────────

age = 20
has_id = True

if age >= 18 and has_id:
    print('Entry allowed')
else:
    print('Entry not allowed')

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print('No school today!')
else:
    print('Go to school!')

is_raining = False

if not is_raining:
    print('Go outside!')
else:
    print('Stay inside!')

# ─────────────────────────────────────
# CONCEPT 5 - Nested If
# ─────────────────────────────────────

age = 25
income = 50000

if age >= 18:
    print('Age requirement met')
    if income >= 30000:
        print('Income requirement met')
        print('Loan approved!')
    else:
        print('Income too low - Loan rejected')
else:
    print('Too young for a loan')

# ─────────────────────────────────────
# CONCEPT 6 - One Line If (Ternary)
# ─────────────────────────────────────

marks = 80
result = 'Pass' if marks >= 40 else 'Fail'
print(result)

weather = 'sunny'
plan = 'Go to park' if weather == 'sunny' else 'Stay home'
print(plan)
