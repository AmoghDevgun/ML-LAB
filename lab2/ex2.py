import pandas as pd

df = pd.read_csv("Employee.csv")

print("Original dataset size:", df.shape)

clean_df = df.dropna()

print("Dataset size after removing missing rows:", clean_df.shape)

