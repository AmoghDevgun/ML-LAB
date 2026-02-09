import pandas as pd

df = pd.read_csv("test_data.csv")

print("number of rows:", df.shape[0])
print("number of columns:", df.shape[1])

print("\nmissing values in each column:")
print(df.isnull().sum())

