# Day 11 - NumPy
# Author: Vishvi
# Date: 2026-07-24

import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.arange(0, 20, 2)
e = np.linspace(0, 1, 5)
f = np.random.randint(1, 100, (3, 3))
print(a, b, c, d, e, f, sep='\n')

# Operations
x = np.array([1, 2, 3, 4, 5])
print(x + 10, x * 2, x ** 2)
print(np.sqrt(x))
print(x.mean(), x.std(), x.min(), x.max())
print(np.sum(x), np.median(x))

# Indexing
m = np.random.randint(1, 10, (4, 4))
print(m[0], m[:, 0], m[1:3, 1:3], m[m > 5])

# Reshape
arr = np.arange(12)
print(arr.reshape(3, 4))

# Broadcasting
matrix   = np.random.randint(1, 10, (3, 3))
row_mean = matrix.mean(axis=1, keepdims=True)
print(matrix - row_mean)

# Stats
data = np.random.randint(50, 100, 20)
print('Mean:', round(data.mean(),2))
print('Median:', np.median(data))
print('Std:', round(data.std(),2))
print('75th percentile:', np.percentile(data, 75))
