# Q1 - NumPy Array Operations (Ashish Pawar, 23I5120)
import numpy as np

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# 4x3 dataset: [MinutesPlayed, Goals, PassAccuracy]
data = np.array([
    [90, 2, 78],
    [85, 1, 82],
    [70, 0, 70],
    [95, 3, 90],
    [60, 0, 65]
])

print("\nOriginal Data:\n", data)
print("\nMean:", np.mean(data))
print("Standard Deviation:", np.std(data))
print("\nTranspose:\n", data.T)
