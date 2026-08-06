# Dataset: Salary Data - Simple Linear Regression
# Kaggle: https://www.kaggle.com/datasets/karthickveerakumar/salary-data-simple-linear-regression
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("karthickveerakumar/salary-data-simple-linear-regression")
df = pd.read_csv(path + "/Salary_Data.csv")

# Box plot of salary data
plt.figure(figsize=(6, 6))
plt.boxplot(df["Salary"], vert=True, patch_artist=True,
            boxprops=dict(facecolor="lightblue"))
plt.title("Box Plot of Salary Data")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()

# Identify outliers using the IQR method
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Number of outliers detected: {len(outliers)}")
print(outliers)
