# Q7 - Advanced Data Cleaning (Ashish Pawar, 23I5120)
import pandas as pd
import numpy as np

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Football players dataset with issues
data = {
    " Player Name ": ["Ronaldo", "Messi", None, "Mbappé", "Kane", "Kane"],
    "Age": [38, 36, 23, 999, 31, 31],       # 999 is outlier
    "Club": ["ALNASSR", "PSG", "PSG", "PSG", "TOT", "TOT"],
    "Goals": [27, np.nan, 15, 28, np.nan, 28]
}

df = pd.DataFrame(data)
print("\nOriginal:\n", df, "\n")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Handle missing names and scores
df["Player_Name"] = df["Player_Name"].fillna("Unknown")
df["Goals"] = df["Goals"].fillna(df["Goals"].mean())

# Handle outlier ages (age > 100)
age_mean = df[df["Age"] < 100]["Age"].mean()
df.loc[df["Age"] > 100, "Age"] = round(age_mean, 2)

# Standardize club names
df["Club"] = df["Club"].str.upper()

print("Cleaned:\n", df)
