import pandas as pd

df = pd.read_csv("Employee.csv")

df.rename(columns={
    "ExperienceInCurrentDomain": "Experience_Years",
    "PaymentTier": "Payment_Tier",
    "LeaveOrNot": "Attrition"
}, inplace=True)

print(df.head())

