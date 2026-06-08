# Python Modules and Libraries

Author: Vishvi
Date: 2026-06-08

---

## What are Modules?

A module is a file containing Python code you can reuse.
Python has thousands of built-in and third-party modules.
You import them to use their features.

---

## Code

```python
# Built-in modules
import math
import random
import datetime
import os
import collections

# math module
print(math.pi)
print(math.sqrt(144))
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.factorial(6))

# random module
print(random.randint(1, 100))
print(random.choice(['Python', 'SQL', 'ML', 'NLP']))
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
print(random.sample(range(100), 5))

# datetime module
now = datetime.datetime.now()
print('Today:', now.strftime('%d-%m-%Y'))
print('Time:', now.strftime('%H:%M:%S'))
print('Year:', now.year)
print('Weekday:', now.strftime('%A'))

# os module
print('Current folder:', os.getcwd())
print('Files here:', os.listdir('.')[:5])

# collections module
from collections import Counter, defaultdict

words = ['python', 'data', 'python', 'science', 'data', 'python']
count = Counter(words)
print('Word counts:', count)
print('Most common:', count.most_common(2))

dd = defaultdict(list)
dd['skills'].append('Python')
dd['skills'].append('SQL')
dd['projects'].append('Titanic')
print(dict(dd))
```

---

## Most Used DS Modules

| Module | What it does |
|---|---|
| numpy | Fast number crunching |
| pandas | Data tables and analysis |
| matplotlib | Charts and graphs |
| seaborn | Beautiful statistical plots |
| sklearn | Machine learning |
| nltk | Natural language processing |
| requests | Fetch data from the web |

---

Built by Vishvi - github.com/vishvi31
