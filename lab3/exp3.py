import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")
numerical_cols = df.select_dtypes(include=np.number).columns

correlation = df[numerical_cols].corr()
covariance = df[numerical_cols].cov()

print("Correlation Matrix:\n", correlation)
print("\nCovariance Matrix:\n", covariance)

