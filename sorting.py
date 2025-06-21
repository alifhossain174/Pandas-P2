import pandas as pd

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 29],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 89, 80]
}

df = pd.DataFrame(data)
df.sort_values(by=["Performance", "Salary"], ascending=[False, True], inplace=True)
print(df)