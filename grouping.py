import pandas as pd

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 27],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 90, 88]
}

df = pd.DataFrame(data)
groupedData = df.groupby("Age")["Salary"].sum()
groupedData2 = df.groupby(["Age", "Performance"])["Salary"].sum()
print(groupedData2)