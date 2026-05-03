import pandas as pd

df = pd.read_csv("diabetes_dataset.csv")

print("Shape of the data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())