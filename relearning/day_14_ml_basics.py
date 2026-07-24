# Day 14 - Machine Learning Basics
# Author: Vishvi
# Date: 2026-07-24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix, accuracy_score)
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris

# Load
iris = load_iris()
df   = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
print(df.head())
print(df['species'].value_counts())

# Split
X = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print('Train:', X_train.shape, '| Test:', X_test.shape)

# Logistic Regression
pipe_lr = Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(max_iter=200))])
pipe_lr.fit(X_train, y_train)
y_pred_lr = pipe_lr.predict(X_test)
print('LR Accuracy:', accuracy_score(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr, target_names=iris.target_names))

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print('RF Accuracy:', accuracy_score(y_test, y_pred_rf))

# Feature Importance
importances = pd.Series(rf.feature_importances_, index=iris.feature_names)
plt.figure(figsize=(8,4))
importances.sort_values().plot(kind='barh', color='steelblue')
plt.title('Feature Importances')
plt.show()

# Confusion Matrix
plt.figure(figsize=(7,5))
sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Cross Validation
cv_lr = cross_val_score(pipe_lr, X, y, cv=5).mean()
cv_rf = cross_val_score(rf,      X, y, cv=5).mean()
print(f'CV Score - LR: {cv_lr:.3f} | RF: {cv_rf:.3f}')

# Predict new
new = np.array([[5.1, 3.5, 1.4, 0.2]])
print('Prediction:', iris.target_names[rf.predict(new)[0]])
