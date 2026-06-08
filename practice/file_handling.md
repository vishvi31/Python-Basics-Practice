# File Handling in Python

Author: Vishvi
Date: 2026-06-08

---

## What is File Handling?

Reading and writing files is how your Python program
saves data permanently. Without file handling,
everything is lost when the program stops.

---

## Code

```python
# Writing to a file
with open('notes.txt', 'w') as f:
    f.write('Python is amazing!\n')
    f.write('File handling is easy.\n')
    f.write('Vishvi is learning Data Science.\n')

print('File written!')

# Reading a file
with open('notes.txt', 'r') as f:
    content = f.read()
print('Full content:\n', content)

# Reading line by line
with open('notes.txt', 'r') as f:
    for i, line in enumerate(f, 1):
        print(f'Line {i}: {line.strip()}')

# Appending to a file
with open('notes.txt', 'a') as f:
    f.write('Appended this new line!\n')

# Reading all lines as a list
with open('notes.txt', 'r') as f:
    lines = f.readlines()
print('Total lines:', len(lines))
print('Lines list:', lines)

# Writing a list to file
skills = ['Python', 'SQL', 'Machine Learning', 'NLP']
with open('skills.txt', 'w') as f:
    for skill in skills:
        f.write(skill + '\n')

# Reading it back
with open('skills.txt', 'r') as f:
    loaded = [line.strip() for line in f.readlines()]
print('Loaded skills:', loaded)
```

---

## Key Modes

| Mode | Meaning |
|---|---|
| r | Read only |
| w | Write (overwrites!) |
| a | Append (adds to end) |
| r+ | Read and write |

---

## Connection to Data Science

- pd.read_csv() uses file handling under the hood
- Saving model results to .txt logs
- Reading config files for ML pipelines
- Saving cleaned datasets back to CSV

---

Built by Vishvi - github.com/vishvi31
