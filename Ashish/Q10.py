# Q10 - Preprocessing and Feature Scaling (Ashish Pawar, 23I5120)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

data = {
    "Player": ["Ronaldo","Messi","Haaland",None,"Kane","Sterling","Unknown"],
    "Age": [38,36,22,29,np.nan,27,30],
    "Goals": [27,25,30,15,18,10,12],
    "Assists": [5,14,7,8,np.nan,6,4],
    "Position": ["Forward","Forward","Forward","Forward","Forward","Winger","Midfield"]
}

df = pd.DataFrame(data)
print("\nOriginal Data:\n", df, "\n")

# Handle missing values
df["Player"] = df["Player"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Assists"] = df["Assists"].fillna(df["Assists"].mean())

# One-hot encode Position
df_encoded = pd.get_dummies(df, columns=["Position"], drop_first=True)

# Split (no target here, just train/test for scaling demonstration)
X_train, X_test = train_test_split(df_encoded.drop("Player", axis=1), test_size=0.3, random_state=42)

cols_to_scale = ["Age", "Goals", "Assists"]
available_cols = [c for c in cols_to_scale if c in X_train.columns]

scaler = StandardScaler()
scaler.fit(X_train[available_cols])

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled[available_cols] = scaler.transform(X_train[available_cols])
X_test_scaled[available_cols] = scaler.transform(X_test[available_cols])

print("Scaled the following columns:", available_cols, "\n")
print("--- Final Scaled Training Data (Head) ---")
print(X_train_scaled.head(), "\n")
print("--- Final Scaled Testing Data (Head) ---")
print(X_test_scaled.head(), "\n")
