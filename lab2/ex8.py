import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")
df.columns = df.columns.str.strip()

plt.scatter(df["Age"], df["PaymentTier"])
plt.xlabel("Age")
plt.ylabel("Payment Tier")
plt.title("Age vs Payment Tier")
plt.show()

