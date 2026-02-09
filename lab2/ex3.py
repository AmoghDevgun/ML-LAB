import pandas as pd

df = pd.read_csv("Employee.csv")

# numerical columns
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["ExperienceInCurrentDomain"] = df["ExperienceInCurrentDomain"].fillna(
    df["ExperienceInCurrentDomain"].median()
)

# categorical columns
df["City"] = df["City"].fillna("Unknown")
df["Gender"] = df["Gender"].fillna("Not Specified")

print(df)
print(df.shape)

