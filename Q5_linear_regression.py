# Q5 - Linear Regression using Scikit-learn

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# --- Student Details ---
student_name = "Shobhit Jain"
roll_number = "23I5165"
# ------------------------

print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Assignment: Q5 - Linear Regression using Scikit-learn\n")

# Step 1: Create / load a dataset
# We'll create a simple dataset where we try to predict 'Marks' based on 'Study Hours'
np.random.seed(42)
study_hours = np.random.randint(1, 10, size=20)
marks = 5 * study_hours + np.random.randint(0, 10, size=20)

df = pd.DataFrame({"Study_Hours": study_hours, "Marks": marks})
print("Sample Data:\n", df.head(), "\n")

# Step 2: Prepare data
X = df[["Study_Hours"]]  # independent variable
y = df["Marks"]          # dependent variable

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Display results
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_, "\n")

print("Predicted vs Actual Values:")
results = pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred})
print(results, "\n")

# Step 6: Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared Score:", r2, "\n")

print("✅ Linear Regression Completed Successfully!")
