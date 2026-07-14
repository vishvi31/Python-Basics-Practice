# Day 7 - File Handling
# Author: Vishvi
# Date: 2026-07-14
# Written by hand in Jupyter Notebook

# ─────────────────────────────────────
# CONCEPT 1 - Writing to a File
# ─────────────────────────────────────

with open('notes.txt', 'w') as f:
    f.write('Hello! This is my first file.\n')
    f.write('I am learning Python.\n')
    f.write('File handling is easy!\n')

print('File written!')

# ─────────────────────────────────────
# CONCEPT 2 - Reading a File
# ─────────────────────────────────────

with open('notes.txt', 'r') as f:
    content = f.read()
print(content)

with open('notes.txt', 'r') as f:
    for line in f:
        print(line.strip())

with open('notes.txt', 'r') as f:
    lines = f.readlines()
print(lines)
print('Total lines:', len(lines))

# ─────────────────────────────────────
# CONCEPT 3 - Appending to a File
# ─────────────────────────────────────

with open('notes.txt', 'a') as f:
    f.write('This line was added later!\n')
    f.write('Appending is useful for logs.\n')

with open('notes.txt', 'r') as f:
    print(f.read())

# ─────────────────────────────────────
# CONCEPT 4 - File Modes
# ─────────────────────────────────────

skills = ['Python', 'SQL', 'Pandas', 'Machine Learning']

with open('skills.txt', 'w') as f:
    for skill in skills:
        f.write(skill + '\n')

with open('skills.txt', 'r') as f:
    loaded = [line.strip() for line in f.readlines()]

print(loaded)
print('Total skills:', len(loaded))

# ─────────────────────────────────────
# CONCEPT 5 - Check if File Exists
# ─────────────────────────────────────

import os

if os.path.exists('notes.txt'):
    print('File exists!')
    print('File size:', os.path.getsize('notes.txt'), 'bytes')
else:
    print('File does not exist!')

files = os.listdir('.')
print('Files here:', files)

# ─────────────────────────────────────
# CONCEPT 6 - Writing and Reading Dictionary
# ─────────────────────────────────────

import json

student = {
    'name':   'Vishvi',
    'age':    23,
    'marks':  92,
    'course': 'Data Science'
}

with open('student.json', 'w') as f:
    json.dump(student, f)

print('Saved!')

with open('student.json', 'r') as f:
    loaded = json.load(f)

print(loaded)
print('Name:', loaded['name'])
print('Marks:', loaded['marks'])

# ─────────────────────────────────────
# MINI PROJECT - Personal Diary
# ─────────────────────────────────────

import datetime

def write_entry():
    date  = datetime.date.today()
    entry = input('Write your diary entry: ')
    with open('diary.txt', 'a') as f:
        f.write(f'\n--- {date} ---\n')
        f.write(entry + '\n')
    print('Entry saved!')

def read_diary():
    try:
        with open('diary.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('No diary entries yet!')

print('===== PERSONAL DIARY =====')
print('1. Write new entry')
print('2. Read all entries')

choice = input('Your choice: ')

if choice == '1':
    write_entry()
elif choice == '2':
    read_diary()
else:
    print('Invalid choice!')
