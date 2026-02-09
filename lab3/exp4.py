import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")
numerical_cols = df.select_dtypes(include=np.number).columns

# Histograms
df[numerical_cols].hist(bins=10, figsize=(10, 6))
plt.suptitle("Histogram of Student Scores")
plt.show()

# Boxplot
df[numerical_cols].plot(kind="box", figsize=(8, 5))
plt.title("Boxplot of Student Scores")
plt.show()

