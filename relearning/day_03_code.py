# Day 3 - For Loops and While Loops
# Author: Vishvi
# Date: 2026-07-07
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Basic For Loop
# ─────────────────────────────────────

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

# ─────────────────────────────────────
# CONCEPT 2 - For Loop with a List
# ─────────────────────────────────────

fruits = ['apple', 'banana', 'mango', 'orange']

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i, fruit)

# ─────────────────────────────────────
# CONCEPT 3 - range with step
# ─────────────────────────────────────

for i in range(0, 20, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
print('Blast off!')

# ─────────────────────────────────────
# CONCEPT 4 - While Loop
# ─────────────────────────────────────

count = 1

while count <= 5:
    print('Count is:', count)
    count += 1

print('Done!')

# ─────────────────────────────────────
# CONCEPT 5 - break and continue
# ─────────────────────────────────────

for i in range(10):
    if i == 5:
        break
    print(i)

print('Loop stopped at 5')

for i in range(10):
    if i == 3:
        continue
    print(i)

print('3 was skipped!')

# ─────────────────────────────────────
# CONCEPT 6 - Nested Loops
# ─────────────────────────────────────

for i in range(1, 4):
    for j in range(1, 4):
        print(i, 'x', j, '=', i*j)
    print('---')

# ─────────────────────────────────────
# MINI PROJECT - Guess My Number Game
# ─────────────────────────────────────

secret   = 7
attempts = 0

print('Guess the number between 1 and 10!')

while True:
    guess = int(input('Your guess: '))
    attempts += 1

    if guess == secret:
        print(f'Correct! You got it in {attempts} attempts!')
        break
    elif guess < secret:
        print('Too low! Try again.')
    else:
        print('Too high! Try again.')
