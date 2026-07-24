# Day 12 - Pandas
# Author: Vishvi
# Date: 2026-07-24

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name':       ['Vishvi','Aditi','Rohan','Priya','Arjun'],
    'age':        [23, 25, 22, 24, 26],
    'score':      [92, 85, 78, 95, 70],
    'department': ['DS','DS','Eng','DS','Eng'],
    'salary':     [50000, 60000, 55000, 70000, 52000]
})

print(df)
print(df.info())
print(df.describe())

# Selection
print(df['name'])
print(df[df['score'] > 85])
print(df[(df['score'] > 80) & (df['department'] == 'DS')])

# New columns
df['bonus']    = df['salary'] * 0.10
df['grade']    = df['score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 75 else 'C')
print(df)

# GroupBy
print(df.groupby('department')['score'].mean())
print(df.groupby('department').agg({'score': ['mean','max'], 'salary': 'sum'}))

# Sorting
print(df.sort_values('score', ascending=False))
print(df.nlargest(3, 'score'))

# Missing values
df_dirty = df.copy()
df_dirty.loc[1, 'score'] = None
print(df_dirty.isnull().sum())
df_clean = df_dirty.fillna({'score': df_dirty['score'].mean()})
print(df_clean)

# Useful methods
print(df['department'].value_counts())
print(df['score'].corr(df['salary']))
