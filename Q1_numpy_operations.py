# Q1 - NumPy Array Operations

import numpy as np

# --- Student Details ---
student_name = "Shobhit Jain"    
roll_number = "23I5165"         
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q1 - NumPy Array Operations\n")

# Create a 2D Array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original Array:\n", arr)

# Mean of the array
mean_value = np.mean(arr)
print("\nMean of array:", mean_value)

# Standard Deviation of the array
std_value = np.std(arr)
print("Standard Deviation of array:", std_value)

# Transpose of the array
transpose_arr = np.transpose(arr)
print("\nTranspose of array:\n", transpose_arr)
