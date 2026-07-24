# Day 13 - Matplotlib and Seaborn
# Author: Vishvi
# Date: 2026-07-24

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name':   ['Vishvi','Aditi','Rohan','Priya','Arjun'],
    'score':  [92, 85, 78, 95, 70],
    'salary': [50000, 60000, 55000, 70000, 52000]
})

# Line chart
x = np.linspace(0, 10, 100)
plt.figure(figsize=(8,4))
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title('Sin and Cos Waves')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(8,4))
plt.bar(df['name'], df['score'], color='steelblue')
plt.title('Student Scores')
plt.show()

# Histogram
plt.figure(figsize=(8,4))
plt.hist(np.random.randn(1000), bins=30, color='coral', edgecolor='black')
plt.title('Normal Distribution')
plt.show()

# Seaborn heatmap
iris = sns.load_dataset('iris')
plt.figure(figsize=(8,6))
sns.heatmap(iris.drop('species',axis=1).corr(), annot=True, cmap='coolwarm')
plt.title('Iris Correlation Heatmap')
plt.show()

# Pairplot
sns.pairplot(iris, hue='species')
plt.show()

# Boxplot
plt.figure(figsize=(8,4))
sns.boxplot(data=iris, x='species', y='sepal_length', palette='Set2')
plt.title('Sepal Length by Species')
plt.show()
