# Q7 - Advanced Data Cleaning using Pandas
# Replace with your own details before submission

import pandas as pd
import numpy as np

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q7 - Advanced Data Cleaning using Pandas\n")

# Step 1: Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", None, "Frank"],
    "Age": [23, 25, 999, 22, np.nan, 24, 26],  # 999 is an outlier
    "Department": ["IT", "it", "CS", "CS", "ECE", "ECE", "ece"],  # inconsistent casing
    "Score": [85, np.nan, 90, 88, 76, 95, np.nan]
}

df = pd.DataFrame(data)
print("Original Data:\n", df, "\n")

# Step 2: Handle missing values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Score"].fillna(df["Score"].mean(), inplace=True)

print("After Handling Missing Values:\n", df, "\n")

# Step 3: Detect and handle outliers (Age > 100 replaced with mean)
age_mean = df[df["Age"] < 100]["Age"].mean()
df.loc[df["Age"] > 100, "Age"] = round(age_mean, 2)

print("After Handling Outliers:\n", df, "\n")

# Step 4: Fix inconsistent data (convert Department to uppercase)
df["Department"] = df["Department"].str.upper()

print("After Fixing Inconsistent Data:\n", df, "\n")

print("✅ Advanced Data Cleaning Completed Successfully!")
