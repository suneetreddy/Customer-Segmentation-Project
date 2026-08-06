import pandas as pd

df = pd.read_csv("Superstore.csv", encoding="latin1")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())