# Q5 - Linear Regression (Ashish Pawar, 23I5120)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

np.random.seed(15)
shots = np.random.randint(20, 100, 40)
conversion = np.random.uniform(0.05, 0.35, 40)
goals = (shots * conversion) + np.random.uniform(-1, 1, 40)

df = pd.DataFrame({"Shots": shots, "Conversion": conversion, "Goals": goals})

X = df[["Shots", "Conversion"]]
y = df["Goals"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_, "\n")
print("Sample Predictions:\n", pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred}).head())
