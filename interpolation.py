import pandas as pd

data = {
    "Name": ["Fahim", None, "Nur"],
    "Age": [27, None, 29],
    "Salary": [25000, None, 60000],
    "Performance": [88, None, 95]
}

df = pd.DataFrame(data)

# df = df.infer_objects(copy=False)
# df.interpolate("linear", axis=0, inplace=True)
df["Age"] = df["Age"].interpolate("linear")
df["Salary"] = df["Salary"].interpolate("linear")
df["Performance"] = df["Performance"].interpolate("linear")
print(df)