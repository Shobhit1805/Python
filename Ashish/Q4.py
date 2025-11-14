# Q4 - Generate Random Data and Save to CSV (Ashish Pawar, 23I5120)
import numpy as np
import pandas as pd

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

np.random.seed(10)
goals = np.random.randint(0, 30, 14)
assists = np.random.randint(0, 15, 14)
shots = np.random.randint(10, 80, 14)

df = pd.DataFrame({
    "Player_ID": np.arange(1, 15),
    "Goals": goals,
    "Assists": assists,
    "Shots": shots
})

print("\nGenerated Random Football Data:\n", df, "\n")
df.to_csv("ashish_random_football_data.csv", index=False)
print("Saved to 'ashish_random_football_data.csv'")
