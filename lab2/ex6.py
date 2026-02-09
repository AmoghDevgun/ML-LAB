import pandas as pd

df = pd.read_csv("Employee.csv")

print("Before correction:")
print(df["Gender"].value_counts())

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female",
    "male": "Male",
    "female": "Female"
})

print("\nAfter correction:")
print(df["Gender"].value_counts())

