import pandas as pd
import math
import xlsxwriter

df = pd.read_json("output.json")
print(df)

newSalary = list()
bonus = list()
for prevSalary in df["Salary"]:
    updatedSalary = prevSalary+math.floor((prevSalary*10)/100)
    newSalary.append(updatedSalary)
    bonus.append(math.floor((updatedSalary*5)/100))

df["Salary"] = newSalary
df["Bonus"] = bonus
print(df)
df.to_excel("output.xlsx", index=False)