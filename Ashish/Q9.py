# Q9 - Random Forest Classifier (Ashish Pawar, 23I5120)
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Football player position classification: 0=Forward, 1=Defender
data = {
    "Speed": [88,92,78,74,95,85,69,80,83,76],
    "Stamina": [90,85,70,65,88,82,60,72,77,68],
    "Tackles": [20,15,55,60,18,22,70,58,40,50],
    "Position": [0,0,1,1,0,0,1,1,0,1]
}

df = pd.DataFrame(data)
X = df.drop("Position", axis=1)
y = df["Position"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test,y_pred), "\n")
print("Classification Report:\n", classification_report(y_test,y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test,y_pred))
