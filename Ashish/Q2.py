# Q2 - Pandas Data Cleaning (Ashish Pawar, 23I5120)
import pandas as pd
import numpy as np

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Dataset with messy columns, missing values, duplicates
data = {
    " Player Name ": ["Kane", "Mbappé", None, "Haaland", "Haaland", "Sterling", "Ben"],
    "Goals ": [18, 25, np.nan, 30, 30, 10, np.nan],
    "Assists": [7, np.nan, 3, 5, 5, 4, 2],
    "Club ": ["TOT", "PSG", "MNC", "MNC", "MNC", "CHE", "CHE"]
}

df = pd.DataFrame(data)
print("\nOriginal Data:\n", df, "\n")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Remove exact duplicates
df = df.drop_duplicates()

# Fill missing values
df["Player_Name"] = df["Player_Name"].fillna("Unknown")
df["Goals"] = df["Goals"].fillna(df["Goals"].mean())
df["Assists"] = df["Assists"].fillna(df["Assists"].mean())

# Standardize club names
df["Club"] = df["Club"].str.upper()

print("Cleaned Data:\n", df)
