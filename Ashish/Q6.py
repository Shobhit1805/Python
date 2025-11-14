# Q6 - Logistic Regression (Ashish Pawar, 23I5120)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Football match outcome dataset
data = {
    "Possession": [55,60,48,50,65,70,40,42,58,62,53,47],
    "ShotsOnTarget": [8,12,5,6,14,9,3,4,10,11,7,5],
    "Fouls": [10,8,12,11,7,6,14,13,9,7,12,10],
    "Win": [1,1,0,0,1,1,0,0,1,1,0,0]
}

df = pd.DataFrame(data)
X = df[["Possession","ShotsOnTarget","Fouls"]]
y = df["Win"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test,y_pred), "\n")
print("Classification Report:\n", classification_report(y_test,y_pred))
