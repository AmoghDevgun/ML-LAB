import pandas as pd
import numpy as np

df = pd.read_csv("StudentsPerformance.csv")
numerical_cols = df.select_dtypes(include=np.number).columns

Q1 = df[numerical_cols].quantile(0.25)
Q2 = df[numerical_cols].quantile(0.50)
Q3 = df[numerical_cols].quantile(0.75)

print("First Quartile (Q1):\n", Q1)
print("\nSecond Quartile (Median / Q2):\n", Q2)
print("\nThird Quartile (Q3):\n", Q3)

