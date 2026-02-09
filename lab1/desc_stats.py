import pandas as pd

df = pd.read_csv("test_data.csv")
summary = df.describe()

print(summary)

