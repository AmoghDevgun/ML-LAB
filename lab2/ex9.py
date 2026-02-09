import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")

plt.hist(df["Age"], bins=8)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

