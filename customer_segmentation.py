import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

df = df.dropna()

customer_data = df.groupby("Customer ID").agg(
    {
        "Sales":"sum",
        "Profit":"sum",
        "Quantity":"sum",
        "Order ID":"count"
    }
)

customer_data.columns=[
    "Total Sales",
    "Total Profit",
    "Total Quantity",
    "Total Orders"
]

print(customer_data.head())