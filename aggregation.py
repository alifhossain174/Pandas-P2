import pandas as pd

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 29],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 89, 80]
}

df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
total_salary = df["Salary"].sum()
min_salary = df["Salary"].min()
max_salary = df["Salary"].max()

print(f"Average Salary : {avg_salary}")
print(f"Total Salary : {total_salary}")
print(f"Minimum Salary : {min_salary}")
print(f"Maximum Salary : {max_salary}")