import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Identify columns
numerical_cols = df.select_dtypes(include=np.number).columns
categorical_cols = df.select_dtypes(exclude=np.number).columns

print("First 5 Rows:\n", df.head())

print("\nNumerical Columns:", numerical_cols)
print("Categorical Columns:", categorical_cols)

# Central Tendency
print("\nMean:\n", df[numerical_cols].mean())
print("\nMedian:\n", df[numerical_cols].median())
print("\nMode:\n", df[numerical_cols].mode().iloc[0])

# Dispersion
print("\nMinimum:\n", df[numerical_cols].min())
print("\nMaximum:\n", df[numerical_cols].max())
print("\nSum:\n", df[numerical_cols].sum())
print("\nVariance:\n", df[numerical_cols].var())
print("\nStandard Deviation:\n", df[numerical_cols].std())

