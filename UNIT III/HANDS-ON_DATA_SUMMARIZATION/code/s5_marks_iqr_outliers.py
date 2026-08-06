# Dataset: Students Performance in Exams
# Kaggle: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
import kagglehub
import pandas as pd

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("spscientist/students-performance-in-exams")
df = pd.read_csv(path + "/StudentsPerformance.csv")

# Detect outliers in math score using the IQR method
Q1 = df["math score"].quantile(0.25)
Q3 = df["math score"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["math score"] < lower_bound) | (df["math score"] > upper_bound)]

print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Number of outlier students detected: {len(outliers)}")
print(outliers[["gender", "math score", "reading score", "writing score"]])
