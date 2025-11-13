# Q3 - Exploratory Data Analysis (EDA)
# Replace with your own details before submission

import pandas as pd

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q3 - EDA using Pandas\n")

# Step 1: Create a simple dataset
data = {
    "Department": ["IT", "IT", "CS", "CS", "ECE", "ECE"],
    "Student_ID": [1, 2, 3, 4, 5, 6],
    "Marks1": [85, 78, 90, 92, 88, 76],
    "Marks2": [80, 82, 91, 89, 85, 79],
    "Attendance": [90, 85, 95, 98, 87, 80]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# Step 2: Display correlation matrix
corr_matrix = df[["Marks1", "Marks2", "Attendance"]].corr()
print("Correlation Matrix:\n", corr_matrix, "\n")

# Step 3: Display group-wise averages by Department
group_avg = df.groupby("Department")[["Marks1", "Marks2", "Attendance"]].mean()
print("Group-wise Averages by Department:\n", group_avg, "\n")

print("✅ EDA Completed Successfully!")
