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

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

scaler=StandardScaler()

scaled_data=scaler.fit_transform(customer_data)

kmeans=KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

customer_data["Cluster"]=kmeans.fit_predict(scaled_data)

print(customer_data.head())

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.scatter(
    customer_data["Total Sales"],
    customer_data["Total Profit"],
    c=customer_data["Cluster"]
)

plt.xlabel("Total Sales")
plt.ylabel("Total Profit")
plt.title("Customer Segments")

plt.show()

print(customer_data.groupby("Cluster").mean())

customer_data.to_csv("Customer_Segments.csv")

print("Customer segmentation completed successfully.")