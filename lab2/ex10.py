import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")
df.columns = df.columns.str.strip()

plt.boxplot(df["Age"])
plt.xlabel("Age")
plt.title("Age Distribution Boxplot")
plt.show()

