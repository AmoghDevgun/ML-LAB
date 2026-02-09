import pandas as pd

data = {
    "name": ["Gayathri", "Ansh", "Vedica", "Ishika"],
    "marks": [100, 100, 99, 69]
}

df = pd.DataFrame(data)
print(df)

print("\ndatatypes:")
print(df.dtypes)

