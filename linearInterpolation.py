import pandas as pd

data = {
    "Time": [1,2,3,4,5,6,7],
    "Value": [10,None,None,None,15,None,100]
}

df = pd.DataFrame(data)
df["Value"] = df["Value"].interpolate(method="linear")
print(df)
