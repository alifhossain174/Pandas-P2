import pandas as pd

data = {
    "Name": ["Fahim", None, "Nur"],
    "Age": [27, None, 29],
    "Salary": [25000, None, 60000],
    "Performance": [88, None, 95]
}

df = pd.DataFrame(data)
# df.dropna(inplace=True)  # Drop rows with any NaN values
# print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)