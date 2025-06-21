import pandas as pd

data = {
    "Name": ["Fahim", None, "Nur"],
    "Age": [27, None, 29],
    "Salary": [25000, None, 60000],
    "Performance": [88, None, 95]
}

df = pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())