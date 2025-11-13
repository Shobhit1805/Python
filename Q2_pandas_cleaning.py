# Q2 - Pandas Data Cleaning

import pandas as pd

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q2 - Pandas Data Cleaning\n")

# Step 1: Create a sample dataset (with missing values, duplicates, and messy columns)
data = {
    " Student ID ": [101, 102, 103, 104, 104],      # duplicate row for 104
    "Name": ["Alice", "Bob", None, "David", "David"],  # missing name for 103
    "Age ": [23, None, 22, 24, 24],                   # missing age for Bob
    "Score (%)": [88, 92, None, 85, 85]               # missing score for 103
}

df = pd.DataFrame(data)
print("Original Data:\n", df, "\n")

# Step 2: Rename columns (remove spaces and special chars)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("%", "pct")
print("After Renaming Columns:\n", df, "\n")

# Step 3: Remove duplicate rows
df = df.drop_duplicates()
print("After Removing Duplicates:\n", df, "\n")

# Step 4: Handle missing values
# Fill missing numeric values with mean, and categorical with "Unknown"
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score_(pct)"] = df["Score_(pct)"].fillna(df["Score_(pct)"].mean())


print("After Handling Missing Values:\n", df, "\n")

print("✅ Data Cleaning Completed Successfully!")
