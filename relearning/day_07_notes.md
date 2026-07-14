# Day 7 - What I Learned

Author: Vishvi
Date: 2026-07-14

---

## Concepts Practiced

| Concept | What it does | Example |
|---|---|---|
| open('f','w') | Write to file | open('notes.txt', 'w') |
| open('f','r') | Read from file | open('notes.txt', 'r') |
| open('f','a') | Append to file | open('notes.txt', 'a') |
| f.write() | Write text | f.write('Hello\n') |
| f.read() | Read all text | content = f.read() |
| f.readlines() | Read as list | lines = f.readlines() |
| with open() | Auto close file | with open() as f: |
| os.path.exists() | Check if file exists | os.path.exists('f.txt') |
| json.dump() | Save dict to file | json.dump(data, f) |
| json.load() | Load dict from file | json.load(f) |

---

## File Modes Cheatsheet

| Mode | Meaning | Warning |
|---|---|---|
| w | Write - creates new file | Deletes existing content! |
| r | Read only | File must exist |
| a | Append - adds to end | Never deletes content |
| r+ | Read and write | File must exist |

---

## Connection to Data Science

| File handling | Data Science equivalent |
|---|---|
| open('data.txt') | pd.read_csv('data.csv') |
| json.dump() | Saving model results |
| json.load() | Loading config files |
| f.readlines() | Reading log files line by line |

---

## Mini Project

Built a Personal Diary app!
- Writes entries with today's date automatically
- Appends so old entries are never deleted
- Reads all entries back cleanly
- Handles missing file with try/except

---

## Tomorrow - Day 8

Topic: OOP - Classes and Objects

---

Built by Vishvi - github.com/vishvi31
