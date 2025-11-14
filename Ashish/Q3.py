# Q3 - EDA (Ashish Pawar, 23I5120)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

student_name = "Ashish Pawar"
roll_number = "23I5120"
print("Student Name:", student_name)
print("Roll Number:", roll_number)

# Football club performance dataset
data = {
    "Club": ["FCB", "FCB", "MCFC", "MCFC", "PSG", "PSG", "RM", "RM"],
    "Goals": [22, 18, 15, 12, 20, 19, 25, 23],
    "Assists": [10, 9, 7, 6, 11, 8, 12, 10],
    "PassAccuracy": [89, 91, 87, 85, 90, 92, 93, 88]
}

df = pd.DataFrame(data)
print("\nDataset:\n", df, "\n")

# Correlation and group-wise averages
corr = df[["Goals", "Assists", "PassAccuracy"]].corr()
print("Correlation Matrix:\n", corr, "\n")

group_avg = df.groupby("Club")[["Goals", "Assists", "PassAccuracy"]].mean()
print("Club-wise Averages:\n", group_avg, "\n")

# Heatmap (saved)
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Club Performance Correlation")
plt.tight_layout()
plt.savefig("ashish_q3_heatmap.png")
plt.show()

# Pairplot (saved)
sns.pairplot(df[["Goals", "Assists", "PassAccuracy"]])
plt.savefig("ashish_q3_pairplot.png")
plt.show()
