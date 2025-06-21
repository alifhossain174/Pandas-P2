import pandas as pd

CuatomerData = {
    "customer_id": [1,2,3],
    "customer_name": ["Fahim", "Jahid Vai", "Rizvi vai"]
}

OrderData = {
    "customer_id": [1,2,4],
    "ordered_amount": [250, 500, 600]
}

df1 = pd.DataFrame(CuatomerData)
df2 = pd.DataFrame(OrderData)

mergedData = pd.merge(df1, df2, on="customer_id", how="outer") # inner outer left right joins
mergedData.fillna("Unknown", inplace=True)
print(mergedData)