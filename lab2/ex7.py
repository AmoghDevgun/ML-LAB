import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")

# Line plot
plt.plot(df["JoiningYear"], df["Age"])
plt.xlabel("Joining Year")
plt.ylabel("Age")
plt.title("Age Trend Over Joining Years")
plt.show()

# Bar plot
df["City"].value_counts().plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Count")
plt.title("Employees by City")
plt.show()

