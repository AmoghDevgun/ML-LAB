import pandas as pd

df = pd.read_csv("test_data.csv")

print("first 5 records:")
print(df.head())

print("\nlast 5 records:")
print(df.tail())

