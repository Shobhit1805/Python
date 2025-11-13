# Q8 - Data Visualization using Matplotlib and Seaborn
# Replace with your own details before submission

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q8 - Data Visualization using Matplotlib and Seaborn\n")

# Step 1: Create a sample dataset
np.random.seed(42)
data = {
    "Department": ["IT", "CS", "ECE", "ME", "EE"],
    "Average_Marks": np.random.randint(60, 95, 5),
    "Attendance": np.random.randint(70, 100, 5)
}

df = pd.DataFrame(data)
print("Dataset:\n", df, "\n")

# Step 2: Bar chart - Average Marks by Department
plt.figure(figsize=(6,4))
plt.bar(df["Department"], df["Average_Marks"], color="skyblue", edgecolor="black")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Step 3: Scatter plot - Attendance vs Marks
plt.figure(figsize=(6,4))
sns.scatterplot(x="Attendance", y="Average_Marks", data=df, color="red", s=80)
plt.title("Scatter Plot: Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.tight_layout()

# Save before showing to make sure it’s written to disk
plt.savefig("scatter_plot.png")
print("✅ Scatter plot saved as 'scatter_plot.png'")
plt.show()


print("✅ Plots created and saved as 'bar_chart.png' and 'scatter_plot.png'")
