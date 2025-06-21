import pandas as pd
import math
import uuid

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 29],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 89, 95]
}

df = pd.DataFrame(data)
print("Initial Data")
print(df)

bonus = list()
employeeId = list()
for salary in df["Salary"]:
    bonus.append(math.floor((salary*5)/100))
    emp_id = f"EMP-{uuid.uuid4().hex[:8].upper()}"
    employeeId.append(emp_id)

# df['bonus'] = df["Salary"] * (5/100)
# print(df.head(2))

df["City"] = ["Dhaka", "Rajshahi", "Khulna"]
df.insert(3, "Bonus", bonus)
df.insert(0, "EmpID", employeeId)
df.to_json("output.json", index=False, orient='records', indent=2)
print(df)

