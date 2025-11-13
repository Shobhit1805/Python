# Q6 - Logistic Regression using Scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q6 - Logistic Regression (Binary Classification)\n")

# Step 1: Create a simple dataset
# Example: Predict whether a student passes (1) or fails (0) based on study hours and attendance
np.random.seed(42)
study_hours = np.random.randint(1, 10, size=20)
attendance = np.random.randint(60, 100, size=20)

# Label: 1 = Pass, 0 = Fail
pass_fail = np.where((study_hours > 4) & (attendance > 75), 1, 0)

df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Pass_Fail": pass_fail
})
print("Dataset:\n", df, "\n")

# Step 2: Split data into features (X) and target (y)
X = df[["Study_Hours", "Attendance"]]
y = df["Pass_Fail"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
acc = accuracy_score(y_test, y_pred)
print("Accuracy of the model:", round(acc, 2), "\n")

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred), "\n")

print("✅ Logistic Regression Completed Successfully!")
