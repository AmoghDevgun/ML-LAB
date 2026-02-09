import pandas as pd

df = pd.read_csv("Employee.csv")

print("Before conversion:")
print(df.dtypes)

df["JoiningYear"] = df["JoiningYear"].astype(int)
df["PaymentTier"] = df["PaymentTier"].astype(int)
df["LeaveOrNot"] = df["LeaveOrNot"].astype(int)

print("\nAfter conversion:")
print(df.dtypes)

