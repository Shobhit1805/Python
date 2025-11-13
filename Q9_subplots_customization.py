# Q9 - Multiple Subplots and Customization using Matplotlib
# Replace with your own details before submission

import numpy as np
import matplotlib.pyplot as plt

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q9 - Multiple Subplots and Customization\n")

# Step 1: Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x / 3) * np.sin(2 * x)
y4 = np.exp(-x / 5) * np.cos(2 * x)

# Step 2: Create subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle("Multiple Subplots Example", fontsize=14, fontweight="bold")

# Step 3: Plot each subplot with customization
axs[0, 0].plot(x, y1, color="blue", linestyle="-", label="sin(x)")
axs[0, 0].set_title("Sine Wave")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(x, y2, color="red", linestyle="--", label="cos(x)")
axs[0, 1].set_title("Cosine Wave")
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(x, y3, color="green", linestyle="-.", label="Damped Sine")
axs[1, 0].set_title("Damped Sine Wave")
axs[1, 0].legend()
axs[1, 0].grid(True)

axs[1, 1].plot(x, y4, color="purple", linestyle=":", label="Damped Cosine")
axs[1, 1].set_title("Damped Cosine Wave")
axs[1, 1].legend()
axs[1, 1].grid(True)

# Step 4: Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.96])  # leaves space for the main title
plt.savefig("subplots_customization.png")
plt.show()

print("✅ Subplots created and saved as 'subplots_customization.png'")
