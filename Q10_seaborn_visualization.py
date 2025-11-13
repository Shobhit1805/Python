# Q10 - Advanced Visualization using Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q10 - Advanced Visualization using Seaborn\n")

# Step 1: Load dataset (Iris)
df = sns.load_dataset("iris")
print("Dataset Preview:\n", df.head(), "\n")

# Step 2: Pairplot - visualize relationships between all numeric features
sns.pairplot(df, hue="species", palette="Set2")
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.savefig("pairplot_iris.png")
plt.show()

# Step 3: Heatmap - correlation between numeric columns
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of Feature Correlations")
plt.tight_layout()
plt.savefig("heatmap_iris.png")
plt.show()

print("✅ Visualizations saved as 'pairplot_iris.png' and 'heatmap_iris.png'")
