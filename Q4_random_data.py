# Q4 - Generate Random Data and Save to CSV

import numpy as np
import pandas as pd

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q4 - Generate Random Data using NumPy and Save to CSV\n")

# Step 1: Generate random data using NumPy
# Let's create random student marks for 10 students in 3 subjects
np.random.seed(42)  # to keep results the same each time
data = np.random.randint(50, 100, size=(10, 3))

# Step 2: Create a Pandas DataFrame
df = pd.DataFrame(data, columns=["Maths", "Science", "English"])
df["Student_ID"] = np.arange(1, 11)

# Step 3: Display the data
print("Generated Random Data:\n", df, "\n")

# Step 4: Save it to a CSV file
csv_filename = "random_student_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ Data saved successfully to '{csv_filename}'")
