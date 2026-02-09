import pandas as pd

df = pd.read_csv("Employee.csv")

print("Missing values (True = missing):")
print(df.isnull())

print("\nNot null values (True = present):")
print(df.notnull())

print("\nTotal missing values in each column:")
print(df.isnull().sum())

