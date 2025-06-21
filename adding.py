import pandas as pd
import math

data = {
    "Name": ["Fahim", "Saad", "Nur"],
    "Age": [27, 28, 29],
    "Salary": [25000, 50000, 60000],
    "Performance": [88, 89, 95]
}

df = pd.DataFrame(data)
df["City"] = ["Dhaka", "Rajshahi", "Khulna"]
# df.to_json("output.json", index=False, orient='records', indent=2)
# print(df)

bonus = list()
for salary in df["Salary"]:
    bonus.append(math.floor((salary*5)/100))

# df['bonus'] = df["Salary"] * (5/100)
# print(df.head(2))

df.insert(3, "Bonus", bonus)
print(df)

