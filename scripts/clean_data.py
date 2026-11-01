
import pandas as pd
import os

# File locations
input_file = "data/raw/electric_vehicles_spec_2025.csv"
output_file = "data/processed/cleaned_ev_data.csv"

print("=" * 50)
print("EV DATA CLEANING")
print("=" * 50)

# Load original dataset
df = pd.read_csv(input_file)

print("\nOriginal dataset:", df.shape)

# Remove rows without a model name
df = df.dropna(subset=["model"])

# Remove duplicate records
df = df.drop_duplicates()

# Remove extra spaces from text columns
for column in df.select_dtypes(include=["object", "string"]).columns:
    df[column] = df[column].str.strip()

# Convert numerical columns to numeric format
numeric_columns = [
    "top_speed_kmh",
    "battery_capacity_kWh",
    "number_of_cells",
    "torque_nm",
    "efficiency_wh_per_km",
    "range_km",
    "acceleration_0_100_s",
    "fast_charging_power_kw_dc",
    "towing_capacity_kg",
    "seats",
    "length_mm",
    "width_mm",
    "height_mm"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Fill small amounts of missing numerical data with median
columns_to_fill = [
    "torque_nm",
    "fast_charging_power_kw_dc",
    "towing_capacity_kg"
]

for column in columns_to_fill:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values
df["fast_charge_port"] = df["fast_charge_port"].fillna("Unknown")
df["cargo_volume_l"] = df["cargo_volume_l"].fillna("Unknown")

# Keep missing number_of_cells values as missing.
# Do not invent battery cell counts.

# Create output directory if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned dataset:", df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nCleaned file saved at:", output_file)
print("\nDATA CLEANING COMPLETED!")
