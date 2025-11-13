# Q10 - Data Preprocessing and Feature Scaling
# Replace with your own details before submission

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q10 - Data Preprocessing and Feature Scaling\n")

# Step 1: Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 30, 22, 28],
    "Department": ["IT", "CS", "CS", "ECE", "IT"],
    "Salary": [50000, 60000, 55000, np.nan, 52000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df, "\n")

# Step 2: Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print("After Handling Missing Values:\n", df, "\n")

# Step 3: Encode categorical column
le = LabelEncoder()
df["Department_Encoded"] = le.fit_transform(df["Department"])
print("After Label Encoding:\n", df, "\n")

# Step 4: Feature Scaling (Standardization)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[["Age", "Salary"]])

df_scaled = pd.DataFrame(
    scaled_features, columns=["Age_Scaled", "Salary_Scaled"]
)
final_df = pd.concat([df, df_scaled], axis=1)

print("Final Preprocessed and Scaled Data:\n", final_df, "\n")

print("✅ Data Preprocessing and Feature Scaling Completed Successfully!")
