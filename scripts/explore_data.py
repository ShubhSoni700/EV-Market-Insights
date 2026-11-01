
import pandas as pd
import os

file_path = "data/raw/electric_vehicles_spec_2025.csv"

print("=" * 50)
print("EV MARKET DATA EXPLORATION")
print("=" * 50)

if not os.path.exists(file_path):
    print("Dataset not found! Check data/raw folder.")
    exit()

df = pd.read_csv(file_path)

print("\n1. Dataset Shape:")
print(df.shape)

print("\n2. Column Names:")
print(df.columns.tolist())

print("\n3. First Five Records:")
print(df.head().to_string())

print("\n4. Data Types:")
print(df.dtypes)

print("\n5. Missing Values:")
print(df.isnull().sum())

print("\n6. Duplicate Records:")
print(df.duplicated().sum())

print("\n7. Numerical Summary:")
print(df.describe())

print("\n8. Unique Manufacturers:")
print(df["brand"].nunique())

print("\nEXPLORATION COMPLETED!")
